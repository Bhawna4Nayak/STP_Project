import streamlit as st

st.title("🔬 Real-time Sensor Parameters")

st.write("Current live readings from IoT sensors:")
st.json({
    "pH": 7.2,
    "Turbidity": "15 NTU",
    "DO": "6.5 mg/L",
    "BOD": "20 mg/L (Predicted)",
    "Flow Rate": "1200 L/hr",
    "Temperature": "28°C"
})
