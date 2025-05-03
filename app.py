import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the model
model = joblib.load('heart_disease_model.pkl')

st.title("Heart Disease Prediction App")

# 1-5
age = st.slider("Age", 20, 80, 45)
sex = st.selectbox("Sex", ['Male', 'Female'])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.slider("Resting Blood Pressure (trestbps)", 90, 200, 120)
chol = st.slider("Serum Cholesterol (chol)", 100, 400, 200)

# 6-10
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.slider("Maximum Heart Rate (thalach)", 60, 210, 150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.slider("ST depression (oldpeak)", 0.0, 6.0, 1.0, step=0.1)

# 11-13
slope = st.selectbox("Slope of ST segment (slope)", [0, 1, 2])
ca = st.selectbox("Number of major vessels (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Encode sex
sex_val = 1 if sex == 'Male' else 0

# Create input array
input_data = np.array([[age, sex_val, cp, trestbps, chol,
                        fbs, restecg, thalach, exang, oldpeak,
                        slope, ca, thal]])

# Predict
if st.button("Predict"):
    result = model.predict(input_data)
    st.success("Prediction: " + ("Heart Disease" if result[0] == 1 else "No Heart Disease"))
