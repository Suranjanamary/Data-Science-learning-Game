import streamlit as st

import theme
from levels import overfitting, sampling, causation

st.set_page_config(page_title="Reef Careers: Finding Fizzy's Dream Job", page_icon="🐟")
theme.inject()

LEVELS = [("l1", "Salary Curve"), ("l2", "Fake Job Census"), ("l3", "Popular Posting Mystery")]


def sidebar_progress():
    scores = st.session_state.get("scores", {})
    st.sidebar.markdown("### 🐚 Shell collection")
    for key, name in LEVELS:
        if st.session_state.get(f"{key}_won"):
            st.sidebar.write(f"🐚 {name} · {scores.get(key, 0)} pts")
        else:
            st.sidebar.write(f"⚪ {name}")
    st.sidebar.markdown(f"**🫧 Pearl points: {sum(scores.values())} / 300**")


def waves():
    st.markdown('<div class="waves">🌊 🐚 🫧 🐟 🫧 🐚 🌊</div>', unsafe_allow_html=True)


def locked(title, needed):
    theme.banner(title, "🔒 Locked")
    st.warning(f"The sea gate is closed. Beat **{needed}** to unlock this level.")


st.sidebar.title("🔱 Reef Careers Academy")
page = st.sidebar.radio(
    "Dive into a level",
    ["🏠 Home", "💼 Level 1: Salary Curve", "🪼 Level 2: Fake Job Census",
     "🔎 Level 3: Popular Posting Mystery"],
)
sidebar_progress()

if all(st.session_state.get(f"l{i}_won") for i in (1, 2, 3)):
    st.sidebar.success("🎉 You found Fizzy's dream job!")

if page == "🏠 Home":
    theme.banner("🐟 Finding Fizzy's Dream Job", "Reef Careers Academy · learn data science by playing")
    waves()
    theme.say("Poseidon", "🔱",
              "Welcome, apprentice! I am **Poseidon**, chief of the Reef Employment Office. "
              "A forgetful little blue fish named **Fizzy** is job hunting on the Great Reef "
              "Job Board, but sneaky jellyfish 🪼 post **fake jobs** to trick job seekers. "
              "Help Fizzy by solving three mysteries. You will **discover** how data science "
              "works by making choices, not by reading answers.")
    theme.say("Fizzy", "🐟",
              "Hi! I'm Fizzy! I'm looking for... what was I looking for? Oh yes, a job! 🫧")
    st.markdown("""
| Level | Mystery | You will discover | Syllabus topic |
|---|---|---|---|
| 💼 1 | Fizzy's Salary Curve | Overfitting vs underfitting | 7. Regression |
| 🪼 2 | The Fake Job Census | Sampling bias and margin of error | 6. Probability & Inferential Statistics |
| 🔎 3 | The Popular Posting Mystery | Correlation is not causation | 5. Descriptive Statistics & EDA |
""")
    st.markdown("""
**How to play**
1. Pick a level from the sidebar (Levels 2 and 3 unlock when you win the previous one).
2. Read the mission, make a choice, and submit it. You have limited attempts.
3. Win to collect a 🐚 shell and score points. Every round uses new random data.
4. After each level, a **reveal** shows what really happened.
""")
elif page == "💼 Level 1: Salary Curve":
    overfitting.run()
elif page == "🪼 Level 2: Fake Job Census":
    if st.session_state.get("l1_won"):
        sampling.run()
    else:
        locked("🪼 Level 2: The Fake Job Census", "Level 1")
else:
    if st.session_state.get("l2_won"):
        causation.run()
    else:
        locked("🔎 Level 3: The Popular Posting Mystery", "Level 2")