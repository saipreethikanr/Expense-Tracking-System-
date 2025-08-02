import streamlit as st
from datetime import datetime
import requests
import pandas as pd

st.title("Expense Management System")

API_URL = "http://127.0.0.1:8000"  

def analytics_tab():

    col1, col2 = st.columns(2)  
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 2)) 
    with col2: 
        end_date = st.date_input("End Date", datetime(2024, 8, 5))
    
    if st.button("Get Analytics "):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics", json=payload)
        response = response.json()
    
        df = pd.DataFrame.from_dict(response).T
        df = df.sort_values(by='percentage', ascending=False)
        st.bar_chart(data=df)
        st.table(df)
