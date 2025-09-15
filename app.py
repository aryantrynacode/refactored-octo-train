import streamlit as st
import pandas as pd
import joblib
from utils.preprocess import preprocess_input

# Load the pre-trained model
model = joblib.load('models/stellar_object_classifier_model.pkl')
# Load the scaler
scaler = joblib.load('models/scaler.joblib')

st.title("🌌 Stellar Object Classifier")
st.write("Predict whether an object is a **Star, Galaxy, or Quasar** using ML")

st.subheader("upload your data file")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:"), df.head()
    df = preprocess_input(df)
    df_scaled = scaler.transform(df)

    label_map = {0: 'Galaxy', 1: 'Quasar', 2: 'Star'}

    predictions = model.predict(df_scaled)
    df['Predicted Class'] = [label_map[p] for p in predictions]
    st.write("Predictions:", df)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label = "Download Predictions as CSV",
        data = csv,
        file_name = "predictions.csv",
        mime= "text/csv",
        key = 'download-csv')
