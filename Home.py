import streamlit as st

# Simple role-based login
def login():
    st.title("🔑 STP Monitoring System - Login")
    role = st.selectbox("Login As", ["Select", "Admin", "Operator"])
    if st.button("Login"):
        if role != "Select":
            st.session_state['role'] = role
            st.success(f"Logged in as {role}")
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.warning("Please select a role to continue")

if 'role' not in st.session_state:
    login()
else:
    st.success(f"Already logged in as {st.session_state['role']}")
    st.switch_page("pages/1_Dashboard.py")
