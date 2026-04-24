import streamlit as st
import pandas as pd

st.title("📈 LSTM Prediction App")

input_data = st.text_input("Enter 3 values")

if st.button("Predict", key="predict_btn"):
    try:
        values = [float(i) for i in input_data.split(",")]

        if len(values) != 3:
            st.error("Enter exactly 3 values")
        else:
            pred_value = sum(values)/3   # simple logic

            st.success(f"Prediction: {pred_value}")

            chart_data = values + [pred_value]
            df = pd.DataFrame(chart_data, columns=["Value"])
            df["Step"] = ["t-3", "t-2", "t-1", "Pred"]
            df = df.set_index("Step")

            st.line_chart(df)

    except:
        st.error("Invalid input")
