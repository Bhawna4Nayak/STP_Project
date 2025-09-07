import streamlit as st

if 'role' in st.session_state and st.session_state['role'] == "Admin":
    st.title("🛠️ Admin Control Panel")
    st.write("Manage system parameters and configurations here.")

    if st.button("Simulate Emergency Shutdown"):
        st.error("⚠️ Plant Shutdown Triggered!")
    if st.button("Reset Alerts"):
        st.success("✅ Alerts Cleared")
else:
    st.title("🔒 Access Denied")
    st.warning("You must be logged in as Admin to view this page.")
