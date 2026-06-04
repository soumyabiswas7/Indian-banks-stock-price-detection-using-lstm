import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model
# load model
model = load_model("bank_lstm_model.h5", compile=False)
scaler = joblib.load("scaler.save")
close_scaler = joblib.load("close_scaler.save")
st.title("Bank Stock Price Predictor")
file = st.file_uploader("Upload CSV")
if file:
    df = pd.read_csv(file)
    df = df.sort_values("Date")
    data = df[["Open","High","Low","Close"]].values
    scaled = scaler.transform(data)
    seq = scaled[-60:].reshape(1,60,4)
    pred = model.predict(seq)
    price = close_scaler.inverse_transform(pred)[0][0]
    st.success(f"Predicted next-day Close: {price:.2f}")