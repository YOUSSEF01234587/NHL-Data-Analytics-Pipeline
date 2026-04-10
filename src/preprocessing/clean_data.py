import pandas as pd
import os

# -------------------------------
# Paths (relative to project root)
# -------------------------------
RAW_DATA_PATH = os.path.join("data", "raw", "nhl_data.csv")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "nhl_data_clean.csv")

# -------------------------------
# Load Raw Data
# -------------------------------
def load_data(path=RAW_DATA_PATH) -> pd.DataFrame:
    """Load raw NHL data from CSV."""
    return pd.read_csv(path)

# -------------------------------
# Clean Data
# -------------------------------
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean NHL data: drop empty columns, fix types, add derived columns."""

    # 1️ Drop completely empty columns
    df = df.dropna(axis=1, how='all')
    
    # 2️ Strip whitespace from column names
    df.columns = df.columns.str.strip()
    
    # 3️ Convert numeric columns and fill missing values with 0
    numeric_cols = ["Wins", "Losses", "OT Losses", "Goals For (GF)", "Goals Against (GA)", "+ / -", "Win %"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # 4️ Ensure text columns are clean
    if "Team Name" in df.columns:
        df["Team Name"] = df["Team Name"].astype(str).str.strip()
    
    # 5️ Add new derived column: Goal Difference
    if "Goals For (GF)" in df.columns and "Goals Against (GA)" in df.columns:
        df["Goal Difference"] = df["Goals For (GF)"] - df["Goals Against (GA)"]
    
    # 6️ Reorder columns for cleanliness
    cols_order = ["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", 
                  "Goals For (GF)", "Goals Against (GA)", "Goal Difference", "+ / -"]
    df = df[[c for c in cols_order if c in df.columns]]
    
    return df

# -------------------------------
# Save Cleaned Data
# -------------------------------
def save_data(df: pd.DataFrame, path=PROCESSED_DATA_PATH) -> None:
    """Save cleaned data to CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[SUCCESS] Cleaned data saved to → {path}")

# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    print(" Loading raw data...")
    df_raw = load_data()
    
    print(" Cleaning data...")
    df_clean = clean_data(df_raw)
    
    print(" Saving cleaned data...")
    save_data(df_clean)
    
    print("  Data cleaning pipeline completed!")