import mysql.connector
from contextlib import contextmanager

##############################

from logging_setup import setup_logger

logger=setup_logger('db_helper', 'server.log')
logger.info("\n")

###########################

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='expense_manager')
    if connection.is_connected():
        print('connection successful')
    else:
        print('NO CONNECTION')
    
    cursor = connection.cursor(dictionary=True)

    yield cursor
    if commit:
        connection.commit()
    
    connection.close()
    cursor.close()

def fetch_all_record():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        return expenses

def fetch_expense_on_date(expense_date):
    logger.info(f"Fetching expenses for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date=%s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses
    
def insert_into_db(expense_date, amount, category, notes):
    logger.info(f"Inserting expense: {expense_date}, {amount}, {category}, {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s,%s,%s,%s)", (expense_date, amount, category, notes))
        expenses = cursor.fetchall()
        return expenses

def delete_expense_from_date(expense_date):
    logger.info(f"Deleting expenses for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s", (expense_date,))

def fetch_expense_summary(sdate, edate):
    logger.info(f"Fetching expense summary from {sdate} to {edate}")
    with get_db_cursor() as cursor:
        cursor.execute("Select category, sum(amount) as total from expenses where expense_date between %s and %s group by category", (sdate, edate))    
        summary = cursor.fetchall()
        return summary

def fetch_monthly_expense_summary():
    logger.info(f"fetch_expense_summary_by_months")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT month(expense_date) as expense_month, 
               monthname(expense_date) as month_name,
               sum(amount) as total FROM expenses
               GROUP BY expense_month, month_name;
            '''
        )
        data = cursor.fetchall()
        return data



if __name__ == "__main__":
    expenses = fetch_expense_on_date('2024-08-01')
    print(expenses)
    insert_into_db('2024-08-28', 100, 'Food', 'Lunch')
    expenses = fetch_expense_on_date('2024-08-28')
    print(expenses)
    delete_expense_from_date('2024-08-28')
    expenses = fetch_expense_on_date('2024-08-28')
    print(expenses)
    summary = fetch_expense_summary('2024-08-01', '2024-08-05')
    print(summary)
    insert_into_db('2024-08-08', 9999, 'Food', 'Dinner')
    expenses = fetch_expense_on_date('2024-08-28')
    print(expenses)
