# Indian Banks Stock Price Prediction Using LSTM

## Overview

This project uses a Long Short-Term Memory (LSTM) neural network to predict stock prices of major Indian public sector banks based on historical market data.

The model was trained using approximately 15 years of stock market data from the following banks:

* State Bank of India (SBI)
* Bank of Baroda (BOB)
* Punjab National Bank (PNB)
* Canara Bank
* Union Bank of India

A Streamlit-based web application is provided to allow users to upload stock data and generate predictions using the trained model.

---

## Features

* Stock price prediction using LSTM
* Trained on 15 years of historical banking stock data
* Streamlit web interface
* CSV file upload support
* Pre-trained TensorFlow/Keras model included
* Data preprocessing using saved scalers

---

## Technology Stack

* Python
* TensorFlow / Keras
* Streamlit
* Pandas
* NumPy
* Joblib

---

## Project Structure

```text
Indian-banks-stock-price-detection-using-lstm/
│
├── app.py                 # Streamlit application
├── bank_lstm_model.h5     # Trained LSTM model
├── scaler.save           # Feature scaler
├── close_scaler.save     # Target scaler
└── README.md
```

---

## Dataset

The model was trained using historical stock market data collected from:

* State Bank of India (SBI)
* Bank of Baroda (BOB)
* Punjab National Bank (PNB)
* Canara Bank
* Union Bank of India

The dataset spans approximately 15 years and includes features such as:

* Open Price
* High Price
* Low Price
* Close Price

---

## Installation

Clone the repository:

```bash
git clone https://github.com/soumyabiswas7/Indian-banks-stock-price-detection-using-lstm.git
cd Indian-banks-stock-price-detection-using-lstm
```

Install dependencies:

```bash
pip install streamlit tensorflow pandas numpy joblib
```

---

## Running the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## Future Improvements

* Multi-bank selection interface
* Interactive stock charts
* Prediction visualization
* Model performance metrics (RMSE, MAE)
* Support for additional Indian banking stocks

---

## Author

Soumya Biswas

B.Tech CSE (AI & ML)

Machine Learning | Deep Learning | Full-Stack Development
