import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Load the model (ensure path and filename are correct)
try:
    model = joblib.load('models/GradientBoosting_nhl_model.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")

st.title("NHL Game Prediction Dashboard")

# 2. Input Fields (using the keys the model expects)
st.sidebar.header("Enter Match Stats")
gf = st.sidebar.number_input("Goals For (GF)", value=0)
ga = st.sidebar.number_input("Goals Against (GA)", value=0)
otl = st.sidebar.number_input("OT Losses", value=0)

# Calculate Goal Difference automatically
goal_diff = gf - ga

if st.button("Predict Outcome"):
    # 3. Construct the DataFrame with the exact feature order used during training
    features = ["Goals For (GF)", "Goals Against (GA)", "Goal Difference", "OT Losses"]
    data = pd.DataFrame([[gf, ga, goal_diff, otl]], columns=features)
    
    # 4. Perform Prediction (Output will be 0 or 1)
    prediction = model.predict(data)[0]
    
    st.subheader("Analysis Results:")
    
    # Logic for displaying results based on classification
    if prediction == 1:
        st.success("Outcome: WINNER! 🎉")
        st.info("The model predicts a victory based on these stats.")
    else:
        st.error("Outcome: LOSER. ❌")
        st.warning("The model predicts a defeat based on these stats.")

    # Show the feature vector for debugging/verification
    with st.expander("Technical Details"):
        st.write("Feature Vector sent to model:")
        st.dataframe(data)
