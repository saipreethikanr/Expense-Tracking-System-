from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

app = FastAPI()

@app.get("/expenses/{expense_date}")
def get_expenses(expense_date: date, response_model=List[Expense]):
    expenses = db_helper.fetch_expense_on_date(expense_date)
    if not expenses:
        return {"message": "No expenses found for this date."}
    return expenses

@app.put("/expenses/{expense_date}")
def update_expense(expense_date: date, expenses: List[Expense]):
    # Delete existing expenses for the given date
    print(expenses)
    db_helper.delete_expense_from_date(expense_date)
    
    # Insert new expenses
    for expense in expenses:
        db_helper.insert_into_db(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully."}

class DateRange(BaseModel):
    start_date: date
    end_date: date
    


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }

    return breakdown

@app.get("/monthly_summary/")
def get_analytics():
    monthly_summary = db_helper.fetch_monthly_expense_summary()
    if monthly_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly expense summary from the database.")

    return monthly_summary
