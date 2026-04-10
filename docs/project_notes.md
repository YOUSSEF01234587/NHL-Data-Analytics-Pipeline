
# NHL Data Analytics - Project Notes

**Prepared by:** Youssef Mohamed Elsayed
**Project:** NHL-Data-Analytics-Pipeline

---

## 1️⃣ Executive Summary

This report summarizes the findings from the **Exploratory Data Analysis (EDA)** on the NHL dataset spanning **1990–2011**.
The goal was to understand team performance distributions, identify key drivers of winning, and observe historical trends in scoring and efficiency.

---

## 2️⃣ Dataset Overview

- **Entries:** 582 rows
- **Columns:** 10 performance metrics per team
- **Timeframe:** 1990 to 2011
- **Key Features:** Wins, Losses, OT Losses, Goals For (GF), Goals Against (GA), Goal Difference
- **Data Integrity:** No missing values – dataset is fully clean

### Descriptive Statistics Highlights

| Metric          | Mean   | Min   | Max   |
| --------------- | ------ | ----- | ----- |
| Wins            | 36.94  | 9     | 62    |
| Win %           | 45.8%  | 11.9% | 75.6% |
| Goals For (GF)  | 234.06 | 115   | 369   |
| Goal Difference | 0      | -196  | 144   |

---

## 3️⃣ Key Findings & Visual Analysis

### A. Distribution of Wins

- Wins follow a **normal (bell-shaped) distribution** centered around **35–45 wins per season**.
- Most professional teams cluster in this range.
- **Elite performances (>50 wins)** and **struggling seasons (<20 wins)** are statistical outliers.

<img src="../data/final/wins_distribution.png" width="600" alt="Wins Distribution">

<img src="../data/final/win_percentage_distribution.png" width="600" alt="Win Percentage Distribution">

---

### B. Correlation Analysis (Drivers of Success)

- **Wins vs Goal Difference (r = 0.82):** Very strong positive correlation – goal difference is the most reliable predictor of wins.
- **Wins vs Losses (r = -0.67):** Expected inverse relationship.
- **OT Losses vs Year (r = 0.86):** Strong upward trend over time, reflecting NHL rule changes and overtime point rewards.

<img src="../data/final/correlation_heatmap.png" width="600" alt="Correlation Heatmap">

---

### C. Performance Trends (1990–2011)

- **Goals For (GF)** shows a dip in the mid-to-late 1990s ("Dead Ball Era") before stabilizing in the 2000s.
- Average team wins remain relatively stable.
- Offensive output fluctuated due to tactical and rule changes.

<img src="../data/final/yearly_trends.png" width="600" alt="Yearly Trends">

---

## 4️⃣ Wins vs Goal Difference Insights

- Teams with **positive Goal Difference** almost always achieve **Win % > 50%**.
- Scatter plot highlights the **linear relationship** between scoring efficiency and wins.
- Year-based color-coding shows that **thresholds for winning shifted slightly** across decades.

<img src="../data/final/wins_vs_goal_difference.png" width="600" alt="Wins vs Goal Difference">

---

## 5️⃣ Model Insights

### A. Gradient Boosting Model Performance

- Best model: **Gradient Boosting**
- Evaluation metrics on test set:
  - **R2 Score:** 0.9337
  - **MAE:** 1.69
  - **RMSE:** 2.30

<img src="../reports/figures/GradientBoosting_feature_importance.png" width="600" alt="Feature Importance">

<img src="../reports/figures/GradientBoosting_feature_importance_eval.png" width="600" alt="Feature Importance Eval">

<img src="../reports/figures/GradientBoosting_pred_vs_actual.png" width="600" alt="Predictions vs Actual">

---

## 6️⃣ Conclusions

- **Offensive/Defensive Balance:** Goal Difference is the critical metric for success. Teams targeting 50+ wins generally need **+50 Goal Difference or higher**.
- **Rule Impact:** Strong correlation between **Year** and **OT Losses** indicates changes in the points system, rewarding overtime performance.
- **Stability Over Time:** Despite fluctuations in scoring, win distributions remain consistent, reflecting competitive balance in the NHL.
- **Modeling Insights:** Gradient Boosting performed best, and the **feature importance plot** shows which team metrics drive predictions.

---

## 7️⃣ Reporting Guidelines

- Include **all plots** at relevant sections (already embedded above).
- Include **descriptive statistics tables**.
- Highlight **correlations visually** with the heatmap.
- Provide **textual insights** with each figure.

---

**Prepared by:** Youssef Mohamed Elsayed
**Project:** NHL-Data-Analytics-Pipeline
