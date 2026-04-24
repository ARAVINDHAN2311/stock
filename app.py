import streamlit as st

st.title("📈 LSTM Prediction App")

input_data = st.text_input("Enter 3 values")

if st.button("Predict"):
    st.success("Prediction: 291.10")   # demo output
import pandas as pd

# inside Predict button
if st.button("Predict"):
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

            # 🔥 GRAPH PART
            chart_data = values + [pred_value]
            df = pd.DataFrame(chart_data, columns=["Value"])

            st.line_chart(df)

    except:
        st.error("Invalid input")
