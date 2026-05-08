import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Data
data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/nhl_data_clean.csv')
df = pd.read_csv(data_path)

# 2. Define Features & Target (Classification)
df['Match_Result'] = (df['Goal Difference'] > 0).astype(int)

features = ["Goals For (GF)", "Goals Against (GA)", "Goal Difference", "OT Losses"]
target = "Match_Result" 

X = df[features]
y = df[target]

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Define Models (Classifiers)
models = {
    "RandomForest": RandomForestClassifier(n_estimators=200, random_state=42),
    "GradientBoosting": GradientBoostingClassifier(n_estimators=200, learning_rate=0.1, random_state=42)
}

# 5. Train & Evaluate
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = {"model": model, "Accuracy": acc}
    print(f"{name} -> Accuracy: {acc:.4f}")

# 6. Select & Save Best Model
best_model_name = max(results, key=lambda x: results[x]["Accuracy"])
best_model = results[best_model_name]["model"]

models_dir = os.path.join(os.path.dirname(__file__), "../../models")
os.makedirs(models_dir, exist_ok=True)
model_path = os.path.join(models_dir, "GradientBoosting_nhl_model.pkl")
joblib.dump(best_model, model_path)
print(f"\nBest Model ({best_model_name}) saved at: {model_path}")
