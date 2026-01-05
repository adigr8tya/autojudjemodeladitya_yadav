import streamlit as st
import joblib

# Load models
classifier = joblib.load("models/classifier.pkl")
regressor = joblib.load("models/regressor.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.set_page_config(page_title="AutoJudge", layout="centered")
st.title("AutoJudge: Programming Problem Difficulty Predictor")

st.write("Paste the problem details below:")

desc = st.text_area("Problem Description")
inp = st.text_area("Input Description")
out = st.text_area("Output Description")

if st.button("Predict Difficulty"):
    combined_text = desc + " " + inp + " " + out
    X_input = vectorizer.transform([combined_text])

    predicted_class = classifier.predict(X_input)[0]
    predicted_score = regressor.predict(X_input)[0]

    st.success(f"Predicted Difficulty Class: **{predicted_class}**")
    st.success(f"Predicted Difficulty Score: **{predicted_score:.2f}**")
