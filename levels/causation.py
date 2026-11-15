import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import theme

N_POSTS = 120
MAX_INVESTIGATIONS = 3
VARIABLES = ["pay_above_market", "company_age", "description_length"]
KINDS = {
    "🎨 Colour the dots by a variable": "colour",
    "⚖️ Control for a variable": "control",
    "📣 Run an experiment (the Job Guild randomly promotes half the postings)": "experiment",
}
OPT_CAUSE = "Lots of applicants cause more scam reports"
OPT_HIDDEN = "A hidden third variable drives both"
OPT_NONE = "There is no relationship at all"


def new_round():
    st.session_state.l3_seed = int(np.random.randint(10000))
    st.session_state.l3_log = []
    st.session_state.l3_verdict = None


def make_data(seed):
    """Pay above market secretly drives BOTH applicants and scam reports."""
    rng = np.random.default_rng(seed)
    pay = rng.uniform(0, 60, N_POSTS)
    age = rng.uniform(1, 30, N_POSTS)
    words = rng.uniform(50, 500, N_POSTS)
    applicants = np.clip(2 * pay + rng.normal(0, 15, N_POSTS), 0, None)
    reports = np.clip(0.1 * pay + rng.normal(0, 0.8, N_POSTS), 0, None)
    return pd.DataFrame({
        "pay_above_market": pay.round(0),
        "company_age": age.round(0),
        "description_length": words.round(0),
        "applicants_per_day": applicants.round(0),
        "scam_reports": reports.round(1),
    })


def partial_corr(df, var):
    """Correlation of applicants and scam reports after removing the effect of var."""
    x, y, z = df["applicants_per_day"], df["scam_reports"], df[var]
    rx = x - np.polyval(np.polyfit(z, x, 1), z)
    ry = y - np.polyval(np.polyfit(z, y, 1), z)
    return float(np.corrcoef(rx, ry)[0, 1])


def experiment(df, seed):
    """The Job Guild promotes a random half of the postings (more applicants).
    Scam reports still come from the pay only, so the real effect of applicants shows."""
    rng = np.random.default_rng(seed + 7)
    promoted = rng.permutation(len(df)) < len(df) // 2
    reports = np.clip(0.1 * df["pay_above_market"].to_numpy() + rng.normal(0, 0.8, len(df)), 0, None)
    return reports[promoted].mean(), reports[~promoted].mean()


def scatter(df, colour_var=None):
    fig, ax = plt.subplots()
    if colour_var:
        sc = ax.scatter(df["applicants_per_day"], df["scam_reports"], c=df[colour_var],
                        cmap="cool", edgecolor="white", s=60)
        fig.colorbar(sc, label=colour_var)
    else:
        ax.scatter(df["applicants_per_day"], df["scam_reports"], color=theme.TEAL,
                   edgecolor="white", s=60)
    ax.set_xlabel("Applicants per day")
    ax.set_ylabel("Scam reports per week")
    return fig


def show_investigation(inv, df, seed):
    kind, var = inv["kind"], inv.get("var")
    if kind == "colour":
        st.pyplot(scatter(df, var))
        st.write(f"Correlation of **{var}** with applicants: "
                 f"**{df[var].corr(df['applicants_per_day']):.2f}**, with scam reports: "
                 f"**{df[var].corr(df['scam_reports']):.2f}**")
    elif kind == "control":
        before = df["applicants_per_day"].corr(df["scam_reports"])
        after = partial_corr(df, var)
        st.write(f"Correlation between applicants and scam reports: **{before:.2f}** "
                 f"before, **{after:.2f}** after removing the effect of **{var}**.")
    else:
        promoted, normal = experiment(df, seed)
        st.write(f"Average scam reports for postings the Guild **promoted** (more applicants): "
                 f"**{promoted:.2f}**. For postings **left alone**: **{normal:.2f}**.")


def run():
    theme.banner("🔎 Level 3: The Popular Posting Mystery",
                 "Syllabus topic 5 · Descriptive Statistics, Visualisation & EDA")
    theme.celebrate_if_needed()
    st.info("🎯 **Learning objective:** explain why two variables can be strongly "
            "correlated without one causing the other, and how to find a hidden "
            "confounding variable.")

    if ("l3_seed" not in st.session_state or "l3_log" not in st.session_state
            or "l3_verdict" not in st.session_state):
        new_round()

    seed = st.session_state.l3_seed
    df = make_data(seed)
    log = st.session_state.l3_log
    verdict = st.session_state.l3_verdict

    theme.say("Fizzy", "🐟",
              "Everyone says: *\"Jobs with lots of applicants get reported as scams more "
              "often!\"* So I should avoid popular jobs, right? ...Or was it the other "
              "way round? I forgot! 🫧")
    theme.say("Poseidon", "🔱",
              f"We recorded **{N_POSTS} postings**. Mermaid detective, you have "
              f"**{MAX_INVESTIGATIONS} investigations** to find the truth. Then give "
              f"your verdict.")

    st.pyplot(scatter(df))
    r = df["applicants_per_day"].corr(df["scam_reports"])
    st.write(f"Correlation between applicants and scam reports: **{r:.2f}**")
    with st.expander("📜 Look at the raw data (pandas DataFrame)"):
        st.dataframe(df)
        st.write(df.describe().round(2))

    left = MAX_INVESTIGATIONS - len(log)
    if left > 0 and verdict is None:
        st.subheader(f"🔎 Investigate ({left} left)")
        kind = KINDS[st.radio("Choose an investigation", list(KINDS))]
        var = st.selectbox("Which variable?", VARIABLES) if kind != "experiment" else None
        if st.button("🔎 Run investigation"):
            log.append({"kind": kind, "var": var})
            st.rerun()

    for i, inv in enumerate(log):
        st.markdown(f"**Investigation {i + 1}:** {inv['kind']}"
                    + (f" ({inv['var']})" if inv["var"] else ""))
        show_investigation(inv, df, seed)

    if log and verdict is None:
        st.subheader("⚖️ Your verdict")
        choice = st.radio("What is going on?", [OPT_CAUSE, OPT_HIDDEN, OPT_NONE])
        hidden = None
        if choice == OPT_HIDDEN:
            hidden = st.selectbox("Which variable is the hidden driver?", VARIABLES,
                                  key="l3_hidden")
        if st.button("🐚 Submit verdict"):
            correct = choice == OPT_HIDDEN and hidden == "pay_above_market"
            found = any(i["var"] == "pay_above_market" and i["kind"] in ("colour", "control")
                        for i in log)
            ran_exp = any(i["kind"] == "experiment" for i in log)
            score = 60 + 20 * found + 20 * ran_exp if correct else 0
            st.session_state.l3_verdict = {"correct": correct, "score": score}
            if correct:
                theme.record("l3", score)
                st.session_state.celebrate = True
            st.rerun()
    elif not log and verdict is None:
        st.caption("Run at least one investigation before giving a verdict.")

    if verdict is not None:
        if verdict["correct"]:
            st.success(f"🔱 Case solved! Score: {verdict['score']} / 100")
        else:
            st.error("Not quite. See the reveal to find out what really happened.")
        st.caption("Scoring: 60 for the right verdict, +20 for checking pay above market, "
                   "+20 for running the experiment.")

        st.subheader("🔍 Reveal: what really happened")
        st.write("**Pay above market** drives both. Jellyfish scammers offer unrealistically "
                 "high pay, which attracts lots of applicants *and* lots of scam reports. "
                 "Having more applicants does not make a posting a scam.")
        st.pyplot(scatter(df, "pay_above_market"))
        st.write(f"Original correlation: **{r:.2f}**")
        st.table(pd.DataFrame({
            "Variable controlled for": VARIABLES,
            "Correlation after controlling": [round(partial_corr(df, v), 2) for v in VARIABLES],
        }).set_index("Variable controlled for"))
        st.markdown(
            "**Takeaway:** correlation does not mean causation. A confounder (pay above "
            "market) can create a strong correlation between two variables that do not "
            "affect each other. Controlling for the right variable makes the correlation "
            "vanish, and a randomised experiment, where we choose which postings get "
            "promoted, shows that more applicants do not cause more scam reports. "
            "**Tip for job seekers:** unusually high pay is the warning sign, not popularity."
        )
        if st.button("🌊 Open a new case"):
            new_round()
            st.rerun()