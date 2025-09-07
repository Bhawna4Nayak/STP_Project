
import streamlit as st
import pandas as pd
import altair as alt

# Simulated real-time data
data = pd.DataFrame({
    'Time': ['10:00', '11:00', '12:00', '13:00'],
    'BOD': [18, 20, 21, 23]
})

# Role-based login
st.title("AI & IoT Sewage Treatment Dashboard")
user_type = st.sidebar.selectbox("Login As", ["Select", "Admin", "Operator"])

if user_type == "Select":
    st.warning("Please select a user role from the sidebar to continue.")
else:
    st.success(f"Logged in as {user_type}")

    st.header("Real-time Parameters")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("pH", "7.2")
        st.metric("Turbidity", "15 NTU")
        st.metric("DO", "6.5 mg/L")
    with col2:
        st.metric("BOD (Predicted)", "20 mg/L")
        st.metric("Flow Rate", "1200 L/hr")

    st.header("Predicted BOD Trend")
    line_chart = alt.Chart(data).mark_line(point=True).encode(
        x='Time',
        y='BOD'
    ).properties(width=600)
    st.altair_chart(line_chart)

    st.header("Anomalies & Alerts")
    st.error("[10:15] Alert: Sudden spike in turbidity above 25 NTU")
    st.warning("[11:05] Warning: DO dropped below threshold")
