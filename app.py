import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import pickle

# load model & scaler
model = load_model("lstm_model.keras")


scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("📈 Stock Price Prediction (LSTM)")

st.write("Enter last 3 Close values")

input_data = st.text_input("Example: 100,102,105")

if st.button("Predict"):
    try:
        values = [float(i) for i in input_data.split(",")]

        if len(values) != 3:
            st.error("Enter exactly 3 values")
        else:
            data = np.array(values).reshape(-1,1)

            # scale
            data = scaler.transform(data)

            # reshape for LSTM
            data = data.reshape(1,3,1)

            # predict
            prediction = model.predict(data)

            # inverse scale
            prediction = scaler.inverse_transform(prediction)

            st.success(f"Predicted Close Price: {prediction[0][0]}")

    except:
        st.error("Invalid input!")
