# src/modeling/evaluate_model.py
import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# -----------------------------
# 1️ Load Data
# -----------------------------
data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/nhl_data_clean.csv')
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Data file not found: {data_path}")

df = pd.read_csv(data_path)

features = ["Goals For (GF)", "Goals Against (GA)", "Goal Difference", "OT Losses"]
target = "Wins"

X = df[features]
y = df[target]

# -----------------------------
# 2️ Load Saved Model
# -----------------------------
models_dir = os.path.join(os.path.dirname(__file__), '../../models/')
model_name = "GradientBoosting_nhl_model.pkl"  # Change if you want a different model
model_path = os.path.join(models_dir, model_name)

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at: {model_path}")

model = joblib.load(model_path)
print(f"Loaded model: {model_name}")

# -----------------------------
# 3️ Predict & Evaluate
# -----------------------------
y_pred = model.predict(X)

r2 = r2_score(y, y_pred)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"\nEvaluation Metrics for {model_name}:")
print(f"R2 Score: {r2:.4f}")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# -----------------------------
# 4️ Feature Importance Visualization (if Tree-Based)
# -----------------------------
if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    plt.figure(figsize=(8,5))
    plt.barh(features, importances, color="skyblue")
    plt.xlabel("Importance")
    plt.title(f"{model_name.split('_')[0]} Feature Importance")
    
    figures_dir = os.path.join(os.path.dirname(__file__), '../../reports/figures/')
    os.makedirs(figures_dir, exist_ok=True)
    fig_path = os.path.join(figures_dir, f"{model_name.split('_')[0]}_feature_importance_eval.png")
    plt.savefig(fig_path, bbox_inches='tight')
    plt.close()
    print(f"Feature importance saved at: {fig_path}")

# -----------------------------
# 5️ Optional: Predictions vs Actual Plot
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(y, y_pred, alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # perfect prediction line
plt.xlabel("Actual Wins")
plt.ylabel("Predicted Wins")
plt.title(f"{model_name.split('_')[0]} Predictions vs Actual")
plot_path = os.path.join(figures_dir, f"{model_name.split('_')[0]}_pred_vs_actual.png")
plt.savefig(plot_path, bbox_inches='tight')
plt.close()
print(f"Predictions vs Actual plot saved at: {plot_path}")