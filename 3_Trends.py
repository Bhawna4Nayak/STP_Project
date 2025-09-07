import streamlit as st
import pandas as pd
import altair as alt

st.title("📈 Parameter Trends")

data = pd.DataFrame({
    "Time": ["Day 1","Day 2","Day 3","Day 4","Day 5"],
    "BOD": [22,20,21,19,18],
    "DO": [6.5,6.2,6.0,5.8,6.1]
})

st.subheader("BOD Trend")
bod_chart = alt.Chart(data).mark_line(point=True).encode(x="Time", y="BOD")
st.altair_chart(bod_chart, use_container_width=True)

st.subheader("DO Trend")
do_chart = alt.Chart(data).mark_line(point=True, color="green").encode(x="Time", y="DO")
st.altair_chart(do_chart, use_container_width=True)
