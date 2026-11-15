# 🐟 How to Play: Finding Fizzy's Dream Job

Welcome to Reef Careers Academy! This guide shows you how to play, with tips if you get stuck.

---

## 🎯 The story

Fizzy is a forgetful little blue fish looking for his dream job on the Great Reef Job Board. But sneaky jellyfish 🪼 post fake jobs! Poseidon needs your help to solve **three mysteries** so Fizzy doesn't fall for a scam.

You will **learn by playing**: make a choice, see what happens, and discover the data science idea yourself.

---

## 🚀 Start the game

1. Open the game link (or run `streamlit run app.py` if you are running it yourself).
2. **Click anywhere on the page once** so the music can start.
3. Use the **sidebar on the left** to choose a level. (On a phone, tap the arrow at the top left to open it.)

---

## 🗺️ The basics

| What you see | What it does |
|---|---|
| **Score bar** (top) | Shows your pearls 🪙, the current world, and shells 🐚 collected out of 3. |
| **World map** (Home page) | Shows your progress. Fizzy 🐟 hops to the next open level, and finished levels turn green. |
| **❓ blocks** (Home page) | Hover over them for a quick tip. |
| **Hit a mystery block** (sidebar) | Press it for a hint about the level you are playing. |
| **Chat bubbles** | Poseidon, Fizzy and others explain the mission and react to your choices. |
| **Rising bubbles** 🫧 | Click them to pop them! It is just for fun. |
| **🎵 and 🔊 buttons** (bottom right) | Turn the music and the sound effects on or off. |

**Rules for every level**

- You have a **limited number of attempts**.
- Some information is **hidden** until you submit your choice.
- Win a level to collect a 🐚 shell and unlock the next level.
- After each level, a **reveal** shows what really happened.
- Every round uses **new random data**, so you can replay for a better score.

---

## 💼 Level 1: Fizzy's Salary Curve

**Your mission:** draw a curve that predicts salary from years of experience, as accurately as possible on **new job offers you cannot see**.

**How to play**

1. Look at the pink dots. They are past job offers.
2. Use the **slider** to choose the curve's complexity (the polynomial degree). Degree 1 is a straight line, and higher degrees wiggle more.
3. Watch the curve change, and watch the **training error** (it is live).
4. Click **Submit this curve** to reveal the hidden error.
5. Get the hidden error **below the target** within **5 attempts**.

**Scoring:** 100 points if you win on your first attempt, down to 20 points on your fifth.

**Tips**

- A curve that touches every dot is not always the best curve.
- If the training error is tiny but the hidden error is big, your curve is **overfitting**.
- If both errors are big, your curve is **underfitting**.
- Read Fizzy's comments after each attempt. They hint at what went wrong.

**You will discover:** more complex is not always better.

---

## 🪼 Level 2: The Fake Job Census

*(Unlocks after you win Level 1.)*

**Your mission:** estimate what **percentage of postings are fake**, to within **±5 percentage points**.

**How to play**

1. Choose how your auditors pick postings:
   - 🕸️ **Random audit:** fair, but costs **3 points** per posting.
   - ⭐ **Top-of-the-feed ads:** cheap, **1 point** per posting.
   - 🏢 **Big-company career pages:** cheap, **1 point** per posting.
2. Use the slider to choose **how many postings** to check. You have a budget of **300 points** per audit.
3. Click **Send the auditors** and read the results.
4. You can run up to **4 audits**. Try different methods and compare!

**Scoring:** 100 points if you win on your first audit, down to 25 points on your fourth.

**Tips**

- Cheap does not always mean good. Think about **who** each method reaches. Would scammers show up more or less often there?
- Compare the estimates from different methods. If they disagree a lot, at least one of them is biased.
- A small **margin of error** does not guarantee a correct answer.

**You will discover:** sample quality beats sample size.

---

## 🔎 Level 3: The Popular Posting Mystery

*(Unlocks after you win Level 2.)*

**Your mission:** postings with more applicants also have more scam reports. Does popularity cause scams? Find out, then give your **verdict**.

**How to play**

1. Look at the scatter plot and the correlation number.
2. You have **3 investigations**. For each one, choose a type:
   - 🎨 **Colour the dots by a variable:** see whether a third variable lines up with both axes.
   - ⚖️ **Control for a variable:** see what happens to the correlation once that variable is accounted for.
   - 📣 **Run an experiment:** the Job Guild randomly promotes half the postings.
3. Choose a variable for the first two types, then click **Run investigation**.
4. When you have enough evidence, choose your **verdict**:
   - Lots of applicants cause more scam reports
   - A hidden third variable drives both (then pick which one!)
   - There is no relationship at all
5. Click **Submit verdict**.

**Scoring (up to 100 points)**

- 60 points for the correct verdict
- +20 points for checking the hidden driver with colouring or controlling
- +20 points for running the experiment

**Tips**

- When two things rise together, ask: *could something else be pushing both?*
- If the correlation drops close to zero after you control for a variable, that variable is a strong suspect.
- An experiment decides things at random, so hidden links cannot sneak in.

**You will discover:** correlation does not mean causation.

---

## 🏆 Winning the game

Win all three levels to collect every 🐚 shell. The world map shows **Poseidon's Palace 🏰** once you have, and the sidebar celebrates Fizzy finding his dream job. The maximum score is **300 pearls**.

---

## ❓ Troubleshooting

| Problem | What to try |
|---|---|
| No sound | Click anywhere on the page once. Check the device volume and the 🎵 / 🔊 buttons. Phones on silent mode may block sound. |
| Level is locked 🔒 | Win the previous level first. |
| The game looks strange or old | Refresh the page. A hard refresh (Ctrl+Shift+R) also works. |
| Everything reset | Progress is kept only while the page stays open. Refreshing starts a new session. |
| I ran out of attempts | Read the reveal, then press the **new round** button to try again with new data. |

Enjoy the dive! 🌊🐚🫧
