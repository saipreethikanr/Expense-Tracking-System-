import streamlit as st
from datetime import datetime
import requests

st.title("Expense Management System")

API_URL = "http://127.0.0.1:8000"  

categories = ["Rent", "Food", "Shopping", "Entertainment", "Transport","Other"]

def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    
    if response.status_code == 200:
        existing_expenses = response.json()
        #st.write(existing_expenses)
    else:
        st.error("Error fetching existing expenses.")
        existing_expenses = []
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Transport", "Other"]
    with st.form(key='expense_form'):

        col1,col2,col3 = st.columns(3)
        with col1:
            st.text("Amount")        
        with col2:
            st.text("Category")
        with col3:
            st.text("Note")

        expenses=[]
        for i in range(5):
            if 'message' in response.json():
                #st.warning("No expenses found for this date.")
                amount = 0.0
                category = "Shopping"
                notes = ""
            elif i < len(existing_expenses):      
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1,col2,col3 = st.columns(3)
            with col1:
                amount = st.number_input(label=f"Amount" ,label_visibility="collapsed", step=1.0, value=amount, key=f"amount_{i}")
                
            with col2:  
                category = st.selectbox(label=f"Category",index=categories.index(category) ,options=categories, label_visibility="collapsed", key=f"category_{i}")

            with col3:                           
                notes = st.text_input(label=f"Notes", label_visibility="collapsed",value=notes, key=f"notes_{i}")

            expenses.append({
                    "amount": amount, 
                    "category": category, 
                    "notes": notes
                })
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            filtered_expenses_array = [expense for expense in expenses if expense['amount'] > 0]
            requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses_array)
            response = requests.put(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses_array)
            if response.status_code == 200:
                st.success("Expenses updated successfully.")
            else:   
                st.error("Error updating expenses.")
            
            pass


