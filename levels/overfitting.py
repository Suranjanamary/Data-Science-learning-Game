import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

import theme

MAX_ATTEMPTS = 5
MAX_DEGREE = 15


def new_round():
    st.session_state.l1_seed = int(np.random.randint(10000))
    st.session_state.l1_attempts = []


def make_data(seed):
    """Past job offers: salary rises quickly with experience, then levels off, plus noise.
    Half the offers are visible (training), half are hidden (test)."""
    rng = np.random.default_rng(seed)
    exp = np.sort(rng.uniform(0, 1, 40))  # 0 to 1 stands for 0 to 10 years
    salary = 35 + 40 * (1 - np.exp(-4 * exp)) + rng.normal(0, 4, 40)  # thousand dollars
    return exp[::2], salary[::2], exp[1::2], salary[1::2]


def fit(deg, x_tr, y_tr, x_te, y_te):
    poly = PolynomialFeatures(deg)
    model = LinearRegression().fit(poly.fit_transform(x_tr[:, None]), y_tr)
    tr = np.sqrt(mean_squared_error(y_tr, model.predict(poly.transform(x_tr[:, None]))))
    te = np.sqrt(mean_squared_error(y_te, model.predict(poly.transform(x_te[:, None]))))
    return poly, model, tr, te


def advice(attempt, target):
    deg, tr, te = attempt["Degree"], attempt["Train error"], attempt["Test error"]
    if te <= target:
        return "My curve predicts the new offers! Wait, what were we doing? Oh yes, I'm getting paid! 🐟"
    if te > 2 * max(tr, 0.5):
        return ("My curve passes through every old offer letter, but it flopped on the new "
                "ones. I think I **memorised the noise**. Maybe try a simpler curve?")
    if deg <= 2:
        return ("My curve is too plain. It misses how pay jumps in the first few years and "
                "then levels off. Maybe it needs a bit more bend?")
    return "Closer, but not quite there. Try another complexity!"


def run():
    theme.banner("💼 Level 1: Fizzy's Salary Curve", "Syllabus topic 7 · Regression")
    theme.celebrate_if_needed()
    st.info("🎯 **Learning objective:** explain why a very complex model can fit the "
            "training data perfectly but predict new data badly (overfitting), and why "
            "a model that is too simple also fails (underfitting).")

    if "l1_seed" not in st.session_state or "l1_attempts" not in st.session_state:
        new_round()

    x_tr, y_tr, x_te, y_te = make_data(st.session_state.l1_seed)
    results = [fit(d, x_tr, y_tr, x_te, y_te)[2:] for d in range(1, MAX_DEGREE + 1)]
    train_curve = [r[0] for r in results]
    test_curve = [r[1] for r in results]
    target = min(test_curve) * 1.25

    theme.say("Poseidon", "🔱",
              f"Fizzy wants to know what salary to expect for his experience. The dots "
              f"you see are **past job offers** on the Reef Job Board. Draw a curve that "
              f"predicts **new offers**, the *hidden* ones. Get the hidden error below "
              f"**{target:.1f} thousand dollars** within **{MAX_ATTEMPTS} attempts**.")
    theme.say("Fizzy", "🐟", "Salary... curve... right! I'll just follow the dots! Easy! 🫧")

    with st.expander("💡 What does the 'degree' mean?"):
        st.write("Degree 1 is a straight line. Higher degrees let the curve bend and "
                 "wiggle more. A wigglier curve follows the dots more closely, but is "
                 "that always good?")

    deg = st.slider("🌀 Curve complexity (polynomial degree)", 1, MAX_DEGREE, 1)
    poly, model, tr, te = fit(deg, x_tr, y_tr, x_te, y_te)

    attempts = st.session_state.l1_attempts
    won = any(a["Test error"] <= target for a in attempts)
    game_over = won or len(attempts) >= MAX_ATTEMPTS

    xs = np.linspace(0, 1, 200)
    fig, ax = plt.subplots()
    ax.scatter(x_tr * 10, y_tr, s=70, color=theme.PINK, edgecolor="white",
               label="past job offers (training)")
    ax.plot(xs * 10, model.predict(poly.transform(xs[:, None])), color=theme.TEAL, lw=3,
            label="your curve")
    ax.set_ylim(20, 95)
    ax.set_xlabel("Years of experience")
    ax.set_ylabel("Salary (thousand dollars)")
    ax.legend()
    st.pyplot(fig)
    st.write(f"Training error (live): **{tr:.2f}**. The hidden error stays secret until you submit.")

    if st.button("🐚 Submit this curve", disabled=game_over):
        attempts.append({"Attempt": len(attempts) + 1, "Degree": deg,
                         "Train error": round(tr, 3), "Test error": round(te, 3)})
        if round(te, 3) <= target:
            st.session_state.celebrate = True
        st.rerun()

    if attempts:
        theme.say("Fizzy", "🐟", advice(attempts[-1], target))
        st.write(f"Attempts used: **{len(attempts)} / {MAX_ATTEMPTS}**")
        st.table(pd.DataFrame(attempts).set_index("Attempt"))
        st.caption("Errors are RMSE in thousands of dollars (lower is better).")

    if game_over:
        if won:
            score = (MAX_ATTEMPTS - len(attempts) + 1) * 20
            theme.record("l1", score)
            st.success(f"🔱 Poseidon is pleased! Score: {score} / 100. Level 2 is unlocked!")
        else:
            st.error("Out of attempts! Check the reveal to see what went wrong.")

        st.subheader("🔍 Reveal: what really happened")
        fig2, ax2 = plt.subplots()
        degs = range(1, MAX_DEGREE + 1)
        ax2.plot(degs, train_curve, marker="o", label="training error")
        ax2.plot(degs, test_curve, marker="o", label="hidden (test) error")
        ax2.axhline(target, linestyle="--", color="gray", label="target")
        ax2.set_yscale("log")
        ax2.set_xlabel("Curve complexity (degree)")
        ax2.set_ylabel("Error, RMSE (log scale)")
        ax2.legend()
        st.pyplot(fig2)
        st.markdown(
            "**Takeaway:** training error keeps falling as the curve gets more complex, "
            "but the hidden error falls and then **rises again**. A very wiggly curve "
            "memorises the random noise in the old offers, so it predicts new offers "
            "badly. That is **overfitting**. A curve that is too simple (low degree) is "
            "**underfitting**. The best model is in the middle."
        )
        if st.button("🌊 Play a new round"):
            new_round()
            st.rerun()