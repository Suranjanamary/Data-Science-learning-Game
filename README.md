# 🐟 Finding Fizzy's Dream Job

### Reef Careers Academy: a game for learning data science concepts

> Fizzy, a forgetful little blue fish, is hunting for a job on the Great Reef Job Board. But sneaky jellyfish 🪼 post **fake jobs** to trick job seekers! Help Fizzy by solving three data science mysteries.

**▶ Play it online:** https://fuzzy-doodle-g46w66wv4gqpfwjp9-8501.app.github.dev/

**📖 How to play:** see [HOW_TO_PLAY.md](HOW_TO_PLAY.md)
**🧪 Playtest evidence:** see [PLAYTEST.md](PLAYTEST.md)

---

## What is this?

This is an interactive game built with Python and Streamlit. Players **discover** data science concepts by making decisions and seeing the results, not by reading about them or answering quiz questions.

In every level:

- the player has a **goal** and a **limited number of attempts**
- some information is **hidden** until the player submits a choice
- their **decisions change the outcome**
- a **reveal** at the end explains what really happened
- every round uses **new random data**, so nothing is hard-coded

---

## Learning objectives and syllabus mapping

| Level | Mystery | Concept | Course topic |
|---|---|---|---|
| 💼 1 | Fizzy's Salary Curve | Overfitting and underfitting | Topic 7: Regression |
| 🪼 2 | The Fake Job Census | Sampling bias and margin of error | Topic 6: Probability & Inferential Statistics |
| 🔎 3 | The Popular Posting Mystery | Correlation vs causation, confounding variables | Topic 5: Descriptive Statistics, Visualisation & Exploratory Analysis |

The code itself also uses material from Topics 2 to 4 (functions and control flow, NumPy arrays, and pandas DataFrames).

### Level 1: Fizzy's Salary Curve (Regression)

**By the end of this level, the player can:**

1. Explain that training error always falls as a model becomes more complex.
2. Explain that test (new data) error falls and then rises again, which is **overfitting**.
3. Recognise that a model that is too simple **underfits**.

**How it works:** the player picks a polynomial degree to predict salary from years of experience. The training error is visible, but the test error stays hidden until they submit. They have 5 attempts to beat a target error.

### Level 2: The Fake Job Census (Probability & Inferential Statistics)

**By the end of this level, the player can:**

1. Explain why a biased sample gives a wrong estimate however large it is.
2. Explain that the margin of error measures random variation only, not bias.
3. Explain why a smaller random sample can beat a bigger convenience sample.

**How it works:** the player estimates the percentage of fake postings on a job board of 10,000 postings. They choose a sampling method (random, top-of-the-feed, or big-company pages) and a sample size within a budget. Random sampling costs 3 points per posting, and the cheaper methods cost 1 but are biased.

### Level 3: The Popular Posting Mystery (Descriptive Statistics & EDA)

**By the end of this level, the player can:**

1. Explain that a strong correlation does not mean one variable causes the other.
2. Use a coloured scatter plot and "controlling for a variable" to look for a hidden confounder.
3. Explain why a randomised experiment can separate cause from correlation.

**How it works:** postings with many applicants also have many scam reports. The player has 3 investigations (colour the dots, control for a variable, or run an experiment) before giving a verdict on what is really going on.

---

## Game design

| Element | How it appears in the game |
|---|---|
| **Goal** | Each level has a clear mission, for example "get the hidden error below the target". |
| **Rules** | Limited attempts, a sampling budget, and a fixed number of investigations. |
| **Feedback** | Character reactions, result tables, charts, and hints (❓ blocks). |
| **Progression** | A world map, with Levels 2 and 3 locked until the previous level is won. |
| **Meaningful decisions** | The choice of model complexity, sampling method, sample size, and investigation changes the outcome. |
| **Discovery** | The reveal at the end of each level shows the concept in a chart, after the player has experienced it. |
| **Scoring** | Up to 100 points per level (300 in total), with more points for fewer attempts. |

### Arcade features

- 🫧 Clickable bubbles that pop with sound effects
- 🧜‍♀️ Swimming mermaids and sea creatures
- 🪙 A Mario-style score bar, world map, and ❓ hint blocks
- 🎵 Background music and sound effects, with on/off buttons (all generated in the browser, so there are no audio files)

---

## Implementation

- **Language:** Python 3
- **Framework:** [Streamlit](https://streamlit.io)
- **Libraries:** NumPy (random data and sampling), pandas (tables), scikit-learn (polynomial regression), Matplotlib (charts)

**Real computation, no hard-coded answers:**

- Level 1 generates noisy salary data with a random seed and fits real polynomial regression models for every degree.
- Level 2 generates a population of 10,000 postings and draws real random and biased samples from it.
- Level 3 generates data with a hidden confounder and computes real correlations, partial correlations, and a simulated randomised experiment.
- Every new round uses a new random seed.

---

## Run it yourself

```bash
# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/Data-Science-learning-Game.git
cd Data-Science-learning-Game

# 2. Install the libraries
pip install -r requirements.txt

# 3. Start the game
streamlit run app.py
```

Then open the link that appears in your terminal (usually http://localhost:8501).

You can also open the repo in **GitHub Codespaces** and run the same two commands (`pip install -r requirements.txt`, then `streamlit run app.py`).

---

## Project structure

```
Data-Science-learning-Game/
├── app.py                  # Menu, world map and level unlocking
├── theme.py                # Ocean-arcade look, music and sound effects
├── requirements.txt        # Python libraries
├── .streamlit/
│   └── config.toml         # Light theme settings
├── levels/
│   ├── __init__.py
│   ├── overfitting.py      # Level 1
│   ├── sampling.py         # Level 2
│   └── causation.py        # Level 3
├── README.md               # This file
├── HOW_TO_PLAY.md          # Player guide
└── PLAYTEST.md             # Peer playtest evidence
```

---

## Documentation and evidence of learning

- **How to play:** [HOW_TO_PLAY.md](HOW_TO_PLAY.md)
- **Learning objectives:** listed above for each level, and shown inside the game at the top of each level
- **Playtest evidence:** [PLAYTEST.md](PLAYTEST.md) records peers who tried the game, their before-and-after answers, their feedback, and the changes made as a result

---

## Credits

- Built with Python, Streamlit, NumPy, pandas, scikit-learn and Matplotlib.
- Pixel font: *Press Start 2P* (Google Fonts, Open Font License).
- All characters (Fizzy, Poseidon, Auditor Crab and others) are original or use standard emoji. Music and sound effects are generated in the browser with the Web Audio API.
- Created as an assignment submission for a data science course.
