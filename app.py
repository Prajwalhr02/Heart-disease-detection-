import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")
st.title("Heart Disease Predictor")

sex_val = 1 if st.selectbox("Sex", ["Male", "Female"]) == "Male" else 0

features = [
    st.slider("Age", 20, 80, 45),
    sex_val,
    st.selectbox("Chest Pain Type", [0, 1, 2, 3]),
    st.slider("Resting BP", 80, 200, 120),
    st.slider("Cholesterol", 100, 400, 200),
    st.selectbox("FBS > 120", [0, 1]),
    st.selectbox("Rest ECG", [0, 1, 2]),
    st.slider("Max HR", 60, 220, 150),
    st.selectbox("Exercise Angina", [0, 1]),
    st.slider("Oldpeak", 0.0, 6.0, 1.0),
    st.selectbox("Slope", [0, 1, 2]),
    st.selectbox("CA", [0, 1, 2, 3]),
    st.selectbox("Thal", [0, 1, 2, 3]),
]

if st.button("Predict"):
    pred = model.predict([features])
    st.success("Prediction: " + ("Heart Disease" if pred[0] == 1 else "No Heart Disease"))
