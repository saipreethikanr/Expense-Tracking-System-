import os
import sys
# Replace this with the absolute path to your backend directory
backend_path = r"l:\SaiPreethika\Projects\2_Expense_tracking"
sys.path.append(backend_path)

from backend import db_helper

def test_fetch_expenses_on_date():
    expenses = db_helper.fetch_expense_on_date('2024-08-15')
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == 'Shopping'
    assert expenses[0]['notes'] == 'Bought potatoes'

def test_fetch_expenses_on_invalid_date():
    expenses = db_helper.fetch_expense_on_date('9999-08-15')
    assert len(expenses) == 0
    
def test_fetch_expenses_summary_date():
    summary = db_helper.fetch_expense_summary('9999-08-01', '9999-08-15')
    assert len(summary) == 0


