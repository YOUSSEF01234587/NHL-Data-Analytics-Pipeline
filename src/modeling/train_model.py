# src/modeling/train_model.py
import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# -----------------------------
# 1️ Load Data
# -----------------------------
data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/nhl_data_clean.csv')
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Data file not found: {data_path}")

df = pd.read_csv(data_path)

# -----------------------------
# 2️ Define Features & Target
# -----------------------------
features = ["Goals For (GF)", "Goals Against (GA)", "Goal Difference", "OT Losses"]
target = "Wins"

X = df[features]
y = df[target]

# -----------------------------
# 3️ Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# 4️ Define Models
# -----------------------------
models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(n_estimators=200, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
}

# -----------------------------
# 5️ Train, Evaluate & Store Results
# -----------------------------
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Fixed RMSE issue
    
    results[name] = {"model": model, "R2": r2, "MAE": mae, "RMSE": rmse}
    
    print(f"{name} -> R2: {r2:.4f}, MAE: {mae:.2f}, RMSE: {rmse:.2f}")

# -----------------------------
# 6️ Select Best Model Based on R2
# -----------------------------
best_model_name = max(results, key=lambda x: results[x]["R2"])
best_model = results[best_model_name]["model"]
print(f"\nBest Model: {best_model_name}")

# -----------------------------
# 7️ Save Best Model
# -----------------------------
models_dir = os.path.join(os.path.dirname(__file__), "../../models")
os.makedirs(models_dir, exist_ok=True)
model_path = os.path.join(models_dir, f"{best_model_name}_nhl_model.pkl")
joblib.dump(best_model, model_path)
print(f"Saved best model at: {model_path}")

# -----------------------------
# 8️ Feature Importance (if Tree-Based)
# -----------------------------
if best_model_name in ["RandomForest", "GradientBoosting"]:
    importances = best_model.feature_importances_
    plt.figure(figsize=(8,5))
    plt.barh(features, importances, color="skyblue")
    plt.xlabel("Importance")
    plt.title(f"{best_model_name} Feature Importance")
    
    reports_fig_dir = os.path.join(os.path.dirname(__file__), "../../reports/figures")
    os.makedirs(reports_fig_dir, exist_ok=True)
    fig_path = os.path.join(reports_fig_dir, f"{best_model_name}_feature_importance.png")
    plt.savefig(fig_path, bbox_inches='tight')
    plt.close()
    print(f"Feature importance saved at: {fig_path}")