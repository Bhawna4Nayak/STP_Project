import streamlit as st

st.title("🚨 Alerts & Anomalies")

alerts = [
    "[10:15] ⚠️ Sudden spike in turbidity above 25 NTU",
    "[11:05] ⚠️ DO dropped below threshold",
    "[13:45] ⚠️ BOD rising above safe limit"
]

for alert in alerts:
    st.error(alert)
