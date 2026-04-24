import streamlit as st

st.title("📈 LSTM Prediction App")

input_data = st.text_input("Enter 3 values")

if st.button("Predict"):
    st.success("Prediction: 291.10")   # demo output
