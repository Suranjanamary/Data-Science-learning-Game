# 🧪 Playtest Report: Finding Fizzy's Dream Job

This file records how real peers tried the game, what they learned, and what I changed because of their feedback.

> ✏️ **TO DO before submitting:** replace every `[...]` placeholder with your real results. Do not invent data. Markers value honest evidence, even if some results are mixed.

---

## 1. Playtest setup

| Item | Details |
|---|---|
| **Date(s)** | [e.g. 12 Nov 2026] |
| **Number of testers** | [3 to 5 peers] |
| **Who they were** | [e.g. classmates in the same course, one friend with no data science background] |
| **How they played** | [e.g. on their own laptop using the deployed link, with me watching] |
| **Time each person played** | [e.g. about 10 to 15 minutes] |
| **Game version tested** | [e.g. commit message or date] |

**Method:** each tester answered a short quiz **before** playing, then played the game **without any help from me**, then answered the **same quiz again** and gave feedback.

---

## 2. Before-and-after questions

Each tester answers these in their own words, once before and once after playing.

| # | Question | Level it relates to |
|---|---|---|
| Q1 | A very complex model fits the training data almost perfectly. Will it always do well on new data? Why or why not? | Level 1 |
| Q2 | A survey asks 10,000 people who all came from one social media group. Is that better than asking 200 randomly chosen people? Why? | Level 2 |
| Q3 | Ice cream sales and drownings are strongly correlated. Does ice cream cause drownings? What else could explain it? | Level 3 |

### Answer guide (what a good answer includes)

- **Q1:** No. A model that is too complex memorises noise in the training data (**overfitting**), so it can do worse on new data. Test error is what matters.
- **Q2:** No. The large group is **biased**, and a bigger biased sample does not fix bias. A smaller **random** sample gives a more trustworthy estimate.
- **Q3:** No. A **confounding variable**, such as hot weather, can drive both. Correlation does not mean causation.

**Scoring:** 0 = wrong or blank, 1 = partly right, 2 = correct with a reason. The maximum total is 6.

---

## 3. Results by tester

### Tester 1: [Name or initials]

| Question | Before (0 to 2) | After (0 to 2) | Notes |
|---|---|---|---|
| Q1 Overfitting | [ ] | [ ] | [what they said] |
| Q2 Sampling | [ ] | [ ] | [what they said] |
| Q3 Causation | [ ] | [ ] | [what they said] |
| **Total (out of 6)** | [ ] | [ ] | |

- **Levels completed:** [e.g. 1, 2 and 3 / only 1 and 2]
- **Attempts used:** [e.g. L1: 3, L2: 2, L3: 3 investigations]
- **Where they got confused:** [...]
- **What they enjoyed:** [...]
- **Memorable quote:** "[...]"

### Tester 2: [Name or initials]

| Question | Before (0 to 2) | After (0 to 2) | Notes |
|---|---|---|---|
| Q1 Overfitting | [ ] | [ ] | [ ] |
| Q2 Sampling | [ ] | [ ] | [ ] |
| Q3 Causation | [ ] | [ ] | [ ] |
| **Total (out of 6)** | [ ] | [ ] | |

- **Levels completed:** [ ]
- **Attempts used:** [ ]
- **Where they got confused:** [ ]
- **What they enjoyed:** [ ]
- **Memorable quote:** "[ ]"

### Tester 3: [Name or initials]

| Question | Before (0 to 2) | After (0 to 2) | Notes |
|---|---|---|---|
| Q1 Overfitting | [ ] | [ ] | [ ] |
| Q2 Sampling | [ ] | [ ] | [ ] |
| Q3 Causation | [ ] | [ ] | [ ] |
| **Total (out of 6)** | [ ] | [ ] | |

- **Levels completed:** [ ]
- **Attempts used:** [ ]
- **Where they got confused:** [ ]
- **What they enjoyed:** [ ]
- **Memorable quote:** "[ ]"

*(Copy the block above for Tester 4 and Tester 5 if you have them.)*

---

## 4. Summary of outcomes

| Tester | Score before (out of 6) | Score after (out of 6) | Change |
|---|---|---|---|
| Tester 1 | [ ] | [ ] | [ ] |
| Tester 2 | [ ] | [ ] | [ ] |
| Tester 3 | [ ] | [ ] | [ ] |
| **Average** | [ ] | [ ] | [ ] |

**What the results show:** [Write 2 to 4 sentences. For example: which concept improved the most, which improved the least, and any tester whose understanding did not change. Be honest about the small sample size.]

---

## 5. Feedback themes

| Theme | How many testers mentioned it | Example comment |
|---|---|---|
| [e.g. Level 2 instructions were unclear] | [ ] | "[ ]" |
| [e.g. Music was fun / too loud] | [ ] | "[ ]" |
| [e.g. Wanted more hints] | [ ] | "[ ]" |
| [ ] | [ ] | "[ ]" |

---

## 6. Changes I made because of the playtest

| # | Problem observed | Evidence (who or what) | Change I made | Commit or date |
|---|---|---|---|---|
| 1 | [e.g. Testers did not understand what "degree" means] | [Testers 1 and 3] | [e.g. Added a "What does degree mean?" expander] | [ ] |
| 2 | [ ] | [ ] | [ ] | [ ] |
| 3 | [ ] | [ ] | [ ] | [ ] |

**Feedback I chose not to act on, and why:** [e.g. "Add more levels", which was out of scope for the time available.]

---

## 7. What I would improve next

- [e.g. Add a fourth level on classification once it is covered in the course]
- [e.g. Add an easy/hard difficulty setting]
- [e.g. Test with more people, including someone with no coding background]

---

## 8. Reflection

[Write a short paragraph: what surprised you while watching people play, and what it taught you about designing a learning game.]

---

### Tips for running a good playtest

1. **Watch quietly.** Do not explain the game while they play. Note where they hesitate or look confused.
2. **Use the deployed link** so they play exactly what the marker will see.
3. **Do the before-quiz first**, and don't show the answer guide until the end.
4. **Take notes straight away**, then write them up here the same day.
5. **Make at least one real change** based on feedback and record it in section 6.
6. **Include honest results.** A tester who didn't improve is still useful evidence.
