import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import theme

POP_SIZE = 10000
BUDGET = 300
MAX_SURVEYS = 4
TOLERANCE = 0.05  # 5 percentage points

METHODS = {
    "🕸️ Random audit": {
        "kind": "random", "cost": 3,
        "desc": "Check randomly chosen postings from the whole board. Slow and costly (3 points per posting)."},
    "⭐ Top-of-the-feed ads": {
        "kind": "feed", "cost": 1,
        "desc": "Check the postings shown first in the feed. Cheap (1 point per posting)."},
    "🏢 Big-company career pages": {
        "kind": "big", "cost": 1,
        "desc": "Check postings from famous big companies. Cheap (1 point per posting)."},
}


def new_round():
    st.session_state.l2_seed = int(np.random.randint(10000))
    st.session_state.l2_surveys = []


def make_board(seed):
    """10,000 postings. Fake ones pay to be promoted (high feed rank) and are rarely from big companies."""
    rng = np.random.default_rng(seed)
    rate = rng.uniform(0.15, 0.30)
    fake = rng.random(POP_SIZE) < rate
    feed = rng.normal(0, 1, POP_SIZE) + 1.5 * fake
    big = rng.normal(0, 1, POP_SIZE) - 2.0 * fake
    return fake, feed, big


def weights(kind, feed, big):
    """How likely each posting is to be checked by each method."""
    if kind == "random":
        return None
    w = np.exp(feed) if kind == "feed" else np.exp(big)
    return w / w.sum()


def draw(kind, feed, big, n, rng):
    return rng.choice(POP_SIZE, size=n, replace=False, p=weights(kind, feed, big))


def convergence(fake, feed, big, seed):
    rng = np.random.default_rng(seed + 999)
    sizes = [10, 30, 100, 300, 1000]
    out = {}
    for name, info in METHODS.items():
        out[name] = [
            np.mean([fake[draw(info["kind"], feed, big, n, rng)].mean() * 100 for _ in range(10)])
            for n in sizes
        ]
    return sizes, out


def run():
    theme.banner("🪼 Level 2: The Fake Job Census", "Syllabus topic 6 · Probability & Inferential Statistics")
    theme.celebrate_if_needed()
    st.info("🎯 **Learning objective:** explain why a biased sample gives a wrong answer "
            "however big it is, and why a smaller random sample can beat a bigger "
            "convenience sample.")

    if "l2_seed" not in st.session_state or "l2_surveys" not in st.session_state:
        new_round()

    fake, feed, big = make_board(st.session_state.l2_seed)
    true_rate = fake.mean()
    surveys = st.session_state.l2_surveys

    theme.say("Poseidon", "🔱",
              f"The Reef Job Board has **{POP_SIZE:,} postings**, and some are fake jobs "
              f"from jellyfish 🪼. Estimate the **percentage of fake postings** to within "
              f"**±{TOLERANCE * 100:.0f} percentage points**. Each audit has a budget of "
              f"**{BUDGET} points**, and you may send auditors **{MAX_SURVEYS} times**. "
              f"I won't reveal the true percentage yet!")
    theme.say("Fizzy", "🐟", "I'll just check the first few ads I see! ...Wait, is that a bad idea? 🫧")

    won = any(abs(s["est"] - true_rate) <= TOLERANCE for s in surveys)
    game_over = won or len(surveys) >= MAX_SURVEYS

    method_name = st.radio("🧭 How will the auditors pick postings?", list(METHODS))
    info = METHODS[method_name]
    st.caption(info["desc"])
    max_n = BUDGET // info["cost"]
    n = st.slider("How many postings?", 10, max_n, min(50, max_n), key=f"l2_n_{info['kind']}")
    st.write(f"💰 Cost: **{n * info['cost']} / {BUDGET}** points")

    if st.button("🦀 Send the auditors", disabled=game_over):
        rng = np.random.default_rng(st.session_state.l2_seed * 100 + len(surveys) + 1)
        idx = draw(info["kind"], feed, big, n, rng)
        k = int(fake[idx].sum())
        p = k / n
        surveys.append({
            "method": method_name, "n": n, "cost": n * info["cost"], "fake_count": k,
            "est": p, "moe": float(1.96 * np.sqrt(p * (1 - p) / n)),
        })
        if abs(p - true_rate) <= TOLERANCE:
            st.session_state.celebrate = True
        st.rerun()

    if surveys:
        last = surveys[-1]
        theme.say("Auditor Crab", "🦀",
                  f"We checked **{last['n']} postings** using *{last['method']}*. "
                  f"**{last['fake_count']}** were fake, so the estimate is "
                  f"**{last['est'] * 100:.1f}%** (margin of error ±{last['moe'] * 100:.1f} points).")
        fig, ax = plt.subplots()
        ax.bar(["Real postings", "Fake postings"], [last["n"] - last["fake_count"], last["fake_count"]],
               color=[theme.TEAL, theme.CORAL])
        ax.set_ylabel("Number of postings in the sample")
        st.pyplot(fig)

        st.write(f"Audits used: **{len(surveys)} / {MAX_SURVEYS}**")
        st.table(pd.DataFrame([{
            "Audit": i + 1, "Method": s["method"], "Postings": s["n"], "Cost": s["cost"],
            "Estimate (% fake)": round(s["est"] * 100, 1),
            "Margin of error (points)": round(s["moe"] * 100, 1),
        } for i, s in enumerate(surveys)]).set_index("Audit"))

    if game_over:
        if won:
            score = (MAX_SURVEYS - len(surveys) + 1) * 25
            theme.record("l2", score)
            st.success(f"🔱 Within ±{TOLERANCE * 100:.0f} points! Score: {score} / 100. Level 3 is unlocked!")
        else:
            st.error("Out of audits! Check the reveal to find out why.")

        st.subheader("🔍 Reveal: what really happened")
        st.write(f"The true percentage of fake postings was **{true_rate * 100:.1f}%**.")
        st.table(pd.DataFrame([{
            "Audit": i + 1, "Method": s["method"], "Postings": s["n"],
            "Estimate (% fake)": round(s["est"] * 100, 1),
            "Error vs truth (points)": round((s["est"] - true_rate) * 100, 1),
        } for i, s in enumerate(surveys)]).set_index("Audit"))

        sizes, out = convergence(fake, feed, big, st.session_state.l2_seed)
        fig2, ax2 = plt.subplots()
        for name, vals in out.items():
            ax2.plot(sizes, vals, marker="o", label=name.split(" ", 1)[1])
        ax2.axhline(true_rate * 100, linestyle="--", color="gray", label="true percentage")
        ax2.set_xscale("log")
        ax2.set_xlabel("Sample size (postings)")
        ax2.set_ylabel("Estimated % fake")
        ax2.legend()
        st.pyplot(fig2)
        st.markdown(
            "**Takeaway:** the random audit homes in on the true percentage as the "
            "sample grows. The convenience samples settle on the **wrong** value: "
            "top-of-the-feed ads **overestimate** fakes (scammers pay to be promoted), "
            "while big-company pages **underestimate** them. Their margins of error "
            "looked small, but the margin of error only measures random chance, not "
            "bias. **Sample quality beats sample size.**"
        )
        if st.button("🌊 Audit a new job board"):
            new_round()
            st.rerun()