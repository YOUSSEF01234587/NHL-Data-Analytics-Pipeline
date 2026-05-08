import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------
# 1️ Load Data & Prepare Target
# -----------------------------
data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/nhl_data_clean.csv')
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Data file not found: {data_path}")

df = pd.read_csv(data_path)

df['Match_Result'] = (df['Goal Difference'] > 0).astype(int)

features = ["Goals For (GF)", "Goals Against (GA)", "Goal Difference", "OT Losses"]
target = "Match_Result"

X = df[features]
y = df[target]

# -----------------------------
# 2️ Load Saved Model
# -----------------------------
models_dir = os.path.join(os.path.dirname(__file__), '../../models/')
model_name = "GradientBoosting_nhl_model.pkl" 
model_path = os.path.join(models_dir, model_name)

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at: {model_path}")

model = joblib.load(model_path)
print(f"Loaded model: {model_name}")

# -----------------------------
# 3️ Predict & Evaluate (Classification Metrics)
# -----------------------------
y_pred = model.predict(X)

accuracy = accuracy_score(y, y_pred)
report = classification_report(y, y)

print(f"\nEvaluation Metrics for {model_name}:")
print(f"Overall Accuracy: {accuracy:.4f}")
print("-" * 30)
print("Classification Report:")
print(report)

# -----------------------------
# 4️ Confusion Matrix Visualization
# -----------------------------
cm = confusion_matrix(y, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Loss', 'Win'], yticklabels=['Loss', 'Win'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title(f'Confusion Matrix: {model_name.split("_")[0]}')

figures_dir = os.path.join(os.path.dirname(__file__), '../../reports/figures/')
os.makedirs(figures_dir, exist_ok=True)
cm_path = os.path.join(figures_dir, 'confusion_matrix.png')
plt.savefig(cm_path)
plt.close()
print(f"Confusion Matrix saved at: {cm_path}")

# -----------------------------
# 5️ Feature Importance
# -----------------------------
if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    plt.figure(figsize=(8,5))
    plt.barh(features, importances, color="skyblue")
    plt.xlabel("Importance Score")
    plt.title(f"Feature Importance ({model_name.split('_')[0]})")
    
    fig_path = os.path.join(figures_dir, f"feature_importance_eval.png")
    plt.savefig(fig_path, bbox_inches='tight')
    plt.close()
    print(f"Feature importance plot saved at: {fig_path}")
