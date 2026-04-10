# 🏒 NHL Data Analytics Pipeline

An end-to-end **Data Analytics & Machine Learning Pipeline** for analyzing NHL team performance and predicting wins using historical statistics.

---

## 📌 Project Overview

This project demonstrates a complete real-world data workflow starting from raw data collection to machine learning model deployment.

The pipeline includes:

* Data Collection & Scraping
* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Machine Learning Modeling
* Model Evaluation
* Visualization & Reporting

---

## 🧱 Project Structure

NHL-DATA-ANALYTICS-PIPELINE/
├── data/
│   ├── final/          # Final visualizations for README
│   ├── processed/      # Cleaned data for modeling
│   └── raw/            # Raw scraped data
├── docs/               # Project notes and documentation
├── models/             # Saved ML models (.pkl)
├── notebooks/          # Jupyter notebooks for EDA
├── reports/
│   ├── figures/        # Model evaluation plots
│   ├── powerbi/        # Power BI dashboard files
│   └── NHL Team Performance.pdf  # Formal Business Report
├── src/                # Source code
│   ├── analysis/
│   ├── modeling/
│   ├── preprocessing/
│   └── scraping/
├── venv/               # Virtual environment
├── README.md
└── requirements.txt

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook
* Power BI

---

## 🔄 Data Pipeline Workflow

### 1️⃣ Data Scraping

**File:** `src/scraping/scraper.py`

Collects NHL statistics data.

---

### 2️⃣ Data Cleaning & Preprocessing

**File:** `src/preprocessing/clean_data.py`

Tasks performed:

* Data validation
* Cleaning inconsistencies
* Feature preparation
* Export clean dataset

Output:

```
data/processed/nhl_data_clean.csv
```

---

### 3️⃣ Exploratory Data Analysis (EDA)

Notebook:

```
notebooks/01_EDA.ipynb
```

---

## 📊 Visual Analysis

### Correlation Heatmap

![]()![Correlation Heatmap](data/final/correlation_heatmap.png)

### Wins Distribution

![]()![Wins Distribution](data/final/wins_distribution.png)

### Win Percentage Distribution

![Win Percentage Distribution](data/final/win_percentage_distribution.png)

### Wins vs Goal Difference

![Wins vs Goal Difference](data/final/wins_vs_goal_difference.png)

### Yearly Performance Trends

![Yearly Trends](data/final/yearly_trends.png)

---

## 🤖 Machine Learning Modeling

Training Script:

```
src/modeling/train_model.py
```

Evaluation Script:

```
src/modeling/evaluate_model.py
```

---

## 🧠 Models Trained

| Model             | Purpose                  |
| ----------------- | ------------------------ |
| Linear Regression | Baseline comparison      |
| Random Forest     | Non-linear relationships |
| Gradient Boosting | Final optimized model    |

---

## 📈 Model Evaluation Results

Metrics Used:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

### Prediction vs Actual

![]()![Prediction vs Actual](reports/figures/GradientBoosting_pred_vs_actual.png)

### Feature Importance

![Feature Importance](reports/figures/GradientBoosting_feature_importance.png)

### Feature Importance (Evaluation)

![Feature Importance Eval](reports/figures/GradientBoosting_feature_importance_eval.png)

---

## 🏆 Best Model Selection

**Gradient Boosting** was selected because:

* Lowest prediction error
* Highest R² score
* Strong handling of nonlinear relationships
* Better generalization on unseen data

Saved Model:

```
models/GradientBoosting_nhl_model.pkl
```

Load model example:

```python
import joblib
model = joblib.load("models/GradientBoosting_nhl_model.pkl")
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUSSEF01234587/NHL-DATA-ANALYTICS-PIPELINE.git
cd NHL-DATA-ANALYTICS-PIPELINE
```

### 2. Set up Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Pipeline

* **Train model:** `python src/modeling/train_model.py`
* **Evaluate model:** `python src/modeling/evaluate_model.py`

---

## 📊 Power BI Dashboard

Power BI files are stored inside:

```
reports/powerbi/
```

Used for interactive analytics and business insights visualization.

---

## 📝 Documentation

Project notes and analysis explanation:

```
docs/project_notes.md
```

---

## 📄 Formal Business Report

You can view the full professional analysis report here: [NHL_Business_Report.pdf](./reports/NHL_Business_Report.pdf)

---

## 🔮 Future Improvements

* Hyperparameter tuning
* Cross-validation pipeline
* Automated ML workflow
* Deployment API
* Real-time dashboard integration

---



## 👨‍💻 Author

**Youssef Mohamed Elsayed** *AI Student at Delta University for Science and Technology | Data Science & Machine Learning Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-talaat-278ba5230/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YOUSSEF01234587) [![Codeforces](https://img.shields.io/badge/Codeforces-445f9d?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/YOUSSEF01234587)
