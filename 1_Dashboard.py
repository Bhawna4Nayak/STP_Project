import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 STP Dashboard Overview")

col1, col2 = st.columns(2)
with col1:
    st.metric("pH", "7.2")
    st.metric("Turbidity", "15 NTU")
with col2:
    st.metric("DO", "6.5 mg/L")
    st.metric("Flow Rate", "1200 L/hr")

# Simulated data
data = pd.DataFrame({
    'Time': ['10:00','11:00','12:00','13:00'],
    'BOD': [18,20,21,23]
})

st.subheader("Predicted BOD Trend")
line_chart = alt.Chart(data).mark_line(point=True).encode(
    x='Time', y='BOD'
)
st.altair_chart(line_chart, use_container_width=True)
