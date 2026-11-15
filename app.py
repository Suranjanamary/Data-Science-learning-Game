import streamlit as st

import theme
from levels import overfitting, sampling, causation

st.set_page_config(page_title="Reef Careers: Finding Fizzy’s Dream Job", page_icon="🐟")
theme.inject()

PAGES = {
    "🏠 Home": ("home", "MAP"),
    "💼 Level 1: Salary Curve": ("l1", "1-1"),
    "🪼 Level 2: Fake Job Census": ("l2", "1-2"),
    "🔎 Level 3: Popular Posting Mystery": ("l3", "1-3"),
}
LEVELS = [("l1", "Salary Curve"), ("l2", "Fake Job Census"), ("l3", "Popular Posting Mystery")]

st.sidebar.title("🔱 REEF CAREERS")
page = st.sidebar.radio("Dive into a level", list(PAGES))
key, world = PAGES[page]

if st.sidebar.button("❓ Hit a mystery block"):
    theme.mystery_block(key)

scores = st.session_state.get("scores", {})
st.sidebar.markdown("### 🐚 Shell collection")
for k, name in LEVELS:
    if st.session_state.get(f"{k}_won"):
        st.sidebar.write(f"🐚 {name} · {scores.get(k, 0)} pts")
    else:
        st.sidebar.write(f"⚪ {name}")
st.sidebar.markdown(f"**🫧 Pearl points: {sum(scores.values())} / 300**")

if all(st.session_state.get(f"l{i}_won") for i in (1, 2, 3)):
    st.sidebar.success("🎉 You found Fizzy’s dream job!")


def locked(title, needed):
    theme.banner(title, "🔒 Locked")
    st.warning(f"The sea gate is closed. Beat **{needed}** to unlock this level.")


if key == "home":
    theme.banner("🐟 Finding Fizzy’s Dream Job", "Reef Careers Academy · learn data science by playing")
    theme.hud(world)
    theme.world_map()
    theme.block_row()
    theme.say("Poseidon", "🔱",
              "Welcome, apprentice! I am **Poseidon**, chief of the Reef Employment Office. "
              "A forgetful little blue fish named **Fizzy** is job hunting on the Great Reef "
              "Job Board, but sneaky jellyfish 🪼 post **fake jobs** to trick job seekers. "
              "Help Fizzy by solving three mysteries. You will **discover** how data science "
              "works by making choices, not by reading answers.")
    theme.say("Fizzy", "🐟",
              "Hi! I’m Fizzy! I’m looking for... what was I looking for? Oh yes, a job! 🫧")
    st.markdown("""
| Level | Mystery | You will discover | Syllabus topic |
|---|---|---|---|
| 💼 1 | Fizzy’s Salary Curve | Overfitting vs underfitting | 7. Regression |
| 🪼 2 | The Fake Job Census | Sampling bias and margin of error | 6. Probability & Inferential Statistics |
| 🔎 3 | The Popular Posting Mystery | Correlation is not causation | 5. Descriptive Statistics & EDA |
""")
    st.markdown("""
**How to play**
1. Pick a level from the sidebar (Levels 2 and 3 unlock when you win the previous one).
2. Read the mission, make a choice, and submit it. You have limited attempts.
3. Win to collect a 🐚 shell and score pearls. Every round uses new random data.
4. After each level, a **reveal** shows what really happened.
5. Stuck? Press **Hit a mystery block** in the sidebar for a hint, and pop bubbles for fun!
""")
elif key == "l1":
    theme.hud(world)
    overfitting.run()
elif key == "l2":
    theme.hud(world)
    if st.session_state.get("l1_won"):
        sampling.run()
    else:
        locked("🪼 Level 2: The Fake Job Census", "Level 1")
else:
    theme.hud(world)
    if st.session_state.get("l2_won"):
        causation.run()
    else:
        locked("🔎 Level 3: The Popular Posting Mystery", "Level 2")