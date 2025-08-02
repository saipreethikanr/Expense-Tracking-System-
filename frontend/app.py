import streamlit as st
from add_update_tab import add_update_tab
from analytics_ui import analytics_tab
from analytics_by_months import analytics_months_tab
st.title("Expense Management System")

API_URL = "http://127.0.0.1:8000"  # Replace with your FastAPI server URL
t1, t2, t3 = st.tabs(['Add/Update Expense', "View Analytics by Category","View Analytics by Month" ])

with t1:
    add_update_tab()

with t2:
    analytics_tab()

with t3:
    analytics_months_tab()
    
def of():
    pass