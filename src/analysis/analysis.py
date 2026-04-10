import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Paths
# -------------------------------
RAW_DATA_PATH = os.path.join("data", "processed", "nhl_data_clean.csv")
FINAL_OUTPUT_DIR = os.path.join("data", "final")

# -------------------------------
# Create output folder if not exists
# -------------------------------
os.makedirs(FINAL_OUTPUT_DIR, exist_ok=True)

# -------------------------------
# Load Data
# -------------------------------
def load_data(path=RAW_DATA_PATH):
    """Load cleaned NHL data."""
    return pd.read_csv(path)

# -------------------------------
# Basic Exploration
# -------------------------------
def explore_data(df):
    """Print basic info and stats."""
    print("\n--- Head of Data ---")
    print(df.head())

    print("\n--- Data Info ---")
    print(df.info())

    print("\n--- Descriptive Stats ---")
    print(df.describe())

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

# -------------------------------
# Visualization
# -------------------------------
def plot_distributions(df):
    """Create and save basic plots."""

    # 1. Distribution of Wins
    plt.figure(figsize=(8,5))
    sns.histplot(df["Wins"], bins=15, kde=True)
    plt.title("Distribution of Wins")
    plt.xlabel("Wins")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(FINAL_OUTPUT_DIR, "wins_distribution.png"))
    plt.close()

    # 2. Wins vs Goal Difference
    plt.figure(figsize=(8,5))
    sns.scatterplot(x="Goal Difference", y="Wins", data=df)
    plt.title("Wins vs Goal Difference")
    plt.xlabel("Goal Difference")
    plt.ylabel("Wins")
    plt.tight_layout()
    plt.savefig(os.path.join(FINAL_OUTPUT_DIR, "wins_vs_goal_difference.png"))
    plt.close()

    # 3. Win % Distribution
    if "Win %" in df.columns:
        plt.figure(figsize=(8,5))
        sns.histplot(df["Win %"], bins=15, kde=True, color="green")
        plt.title("Distribution of Win %")
        plt.xlabel("Win %")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(os.path.join(FINAL_OUTPUT_DIR, "win_percentage_distribution.png"))
        plt.close()

    print(f"\n[INFO] Plots saved to {FINAL_OUTPUT_DIR}")

# -------------------------------
# Main Function
# -------------------------------
def main():
    print("\n[INFO] Loading data...")
    df = load_data()

    print("\n[INFO] Exploring data...")
    explore_data(df)

    print("\n[INFO] Creating visualizations...")
    plot_distributions(df)

    print("\n[INFO] Analysis completed successfully!")

# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    main()