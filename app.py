import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import pickle

model = load_model("lstm_model.keras")
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("📈 LSTM Prediction App")

input_data = st.text_input("Enter 3 values")

if st.button("Predict", key="predict_btn"):
    try:
        values = [float(i) for i in input_data.split(",")]

        if len(values) != 3:
            st.error("Enter exactly 3 values")
        else:
            data = np.array(values).reshape(-1,1)
            data_scaled = scaler.transform(data)
            data_scaled = data_scaled.reshape(1,3,1)

            prediction = model.predict(data_scaled)
            prediction = scaler.inverse_transform(prediction)

            pred_value = prediction[0][0]

            st.success(f"Prediction: {pred_value}")

            # Graph
            chart_data = values + [pred_value]
            df = pd.DataFrame(chart_data, columns=["Value"])
            df["Step"] = ["t-3", "t-2", "t-1", "Pred"]
            df = df.set_index("Step")

            st.line_chart(df)

    except:
        st.error("Invalid input")
