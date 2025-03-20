import streamlit as st
import requests
import json
import time  # For animation effect

# Define API URL
API_URL = "http://127.0.0.1:5000/predict"  # Ensure Flask API is running

# Streamlit UI Design
st.set_page_config(page_title="Wine Quality Predictor", page_icon="🍷", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f4f4;
    }
    .stButton>button {
        background-color: #8B0000;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for Inputs
st.sidebar.title("🍇 Wine Features")
st.sidebar.write("Enter wine characteristics below:")

# Input fields for all features
fixed_acidity = st.sidebar.number_input("Fixed Acidity", min_value=0.0, step=0.1)
volatile_acidity = st.sidebar.number_input("Volatile Acidity", min_value=0.0, step=0.01)
citric_acid = st.sidebar.number_input("Citric Acid", min_value=0.0, step=0.01)
residual_sugar = st.sidebar.number_input("Residual Sugar", min_value=0.0, step=0.1)
chlorides = st.sidebar.number_input("Chlorides", min_value=0.0, step=0.001, format="%.4f")
free_sulfur_dioxide = st.sidebar.number_input("Free Sulfur Dioxide", min_value=0.0, step=1.0)
total_sulfur_dioxide = st.sidebar.number_input("Total Sulfur Dioxide", min_value=0.0, step=1.0)
density = st.sidebar.number_input("Density", min_value=0.0, step=0.0001, format="%.5f")
pH = st.sidebar.number_input("pH", min_value=0.0, step=0.01)
sulphates = st.sidebar.number_input("Sulphates", min_value=0.0, step=0.01)
alcohol = st.sidebar.number_input("Alcohol", min_value=0.0, step=0.1)

# Main Section
st.title("🍷 Wine Quality Prediction")
st.write("Predict the quality of wine based on its chemical composition.")

# Prediction Button
if st.sidebar.button("🍷 Predict Quality"):
    input_data = {
        "features": [
            fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
            free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol
        ]
    }

    with st.spinner("🔄 Analyzing..."):
        time.sleep(1)  # Simulate delay

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            wine_quality = result["wine_quality"]

            # Display animated success message
            st.success(f"✅ Predicted Wine Quality: **{wine_quality}**")
            st.balloons()

        else:
            st.error("⚠️ Error in prediction! Make sure the Flask API is running.")

    except requests.exceptions.ConnectionError:
        st.error("❌ Unable to connect to the API. Make sure the Flask app is running.")

# Footer
st.markdown("---")
st.caption("Developed with using Streamlit")
