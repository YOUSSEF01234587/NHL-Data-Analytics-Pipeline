# 🏒 NHL Data Analytics Pipeline

An end-to-end **Data Analytics & Machine Learning Pipeline** for analyzing NHL team performance and predicting wins using historical statistics.

---

## 📌 Project Overview

💡 This project demonstrates how data-driven insights can be used to improve team performance prediction and decision-making in sports analytics.

### 🔄 The pipeline includes:

* Data Collection & Scraping
* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Machine Learning Modeling
* Model Evaluation
* Visualization & Reporting

---

## 🧱 Project Structure

```text
NHL-DATA-ANALYTICS-PIPELINE/
├── data/
│   ├── final/              # Final visualizations for README
│   ├── processed/          # Cleaned data for modeling
│   └── raw/                # Raw scraped data
├── docs/                   # Project notes and documentation
├── models/                 # Saved ML models (.pkl)
├── notebooks/              # Jupyter notebooks for EDA
├── reports/
│   ├── figures/            # Model evaluation plots
│   ├── powerbi/            # Power BI dashboard files
│   └── NHL Team Performance.pdf
├── src/
│   ├── analysis/
│   ├── modeling/
│   ├── preprocessing/
│   └── scraping/
├── venv/                   # Virtual environment
├── README.md
└── requirements.txt
```
---

## ⚙️ Technologies Used

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Joblib
* **Tools:** Jupyter Notebook, Power BI, Git

---

## 🔄 Data Pipeline Workflow

### 1️⃣ Data Scraping

**File:** `src/scraping/scraper.py`

* Collects NHL statistics and team data

---

### 2️⃣ Data Cleaning & Preprocessing

**File:** `src/preprocessing/clean_data.py`

* Handles missing values
* Feature engineering
* Output file:

```text
data/processed/nhl_data_clean.csv
```

---

### 3️⃣ Exploratory Data Analysis (EDA)

**Notebook:** `notebooks/01_EDA.ipynb`

* Understanding distributions
* Detecting patterns & relationships

---

## 📊 Visual Analysis

|               Correlation Heatmap               |            Wins Distribution            |
| :----------------------------------------------: | :-------------------------------------: |
| ![Correlation](data/final/correlation_heatmap.png) | ![Wins](data/final/wins_distribution.png) |

|                   Win Percentage                   |                Wins vs Goal Difference                |
| :------------------------------------------------: | :---------------------------------------------------: |
| ![Win %](data/final/win_percentage_distribution.png) | ![Wins vs Goal](data/final/wins_vs_goal_difference.png) |

---

## 🤖 Machine Learning Modeling

**Training:** `src/modeling/train_model.py`

**Evaluation:** `src/modeling/evaluate_model.py`

### 🧠 Models Trained

| Model             | Purpose                     |
| ----------------- | --------------------------- |
| Linear Regression | Baseline comparison         |
| Random Forest     | Capturing non-linear trends |
| Gradient Boosting | Final optimized model       |

### 📈 Model Performance


![Actual vs Predicted](reports/figures/GradientBoosting_pred_vs_actual.png)
*Comparison between Predicted and Actual wins.*

![Feature Importance](reports/figures/GradientBoosting_feature_importance.png)
*Key factors influencing the model's decisions.*

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUSSEF01234587/NHL-DATA-ANALYTICS-PIPELINE.git
cd NHL-DATA-ANALYTICS-PIPELINE
```

### 2️⃣ Set up Virtual Environment

#### 🪟 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---



## 🔗 Connect With Me

* 💼 LinkedIn:

  👉 [https://www.linkedin.com/in/youssef-talaat-278ba5230/](https://www.linkedin.com/in/youssef-talaat-278ba5230/)
* 💻 Codeforces:

  👉 [https://codeforces.com/profile/yousef1234556](https://codeforces.com/profile/yousef1234556)

---

## 👨‍💻 Author

**Youssef Mohamed Elsayed**

*AI Student at Delta University | Data Science & Machine Learning Enthusiast*
