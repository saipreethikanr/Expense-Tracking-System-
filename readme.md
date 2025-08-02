# Expense Tracking System



Welcome to the **Expense Tracker** project! This application helps you manage your daily expenses effectively. It combines a user-friendly Streamlit frontend, a robust FastAPI backend, and an SQL database for seamless data handling. 



## Project Overview

This project is an expense management system designed to assist users in tracking their expenses. With this application, users can:

- Record daily expenses
- View analytics on spending
- Interact with a SQL database for data storage and retrieval

The application aims to simplify expense tracking and provide valuable insights into spending habits.

## Features

- **User Authentication**: Secure user login to keep your data private.
- **Expense Tracking**: Easily add, edit, and delete expenses.
- **Analytics Dashboard**: Visualize your spending patterns with graphs and charts.
- **Data Storage**: Use SQL for reliable data storage and retrieval.
- **Responsive Design**: Access the application on various devices.

## Technologies Used

This project utilizes several key technologies:

- **Frontend**: Streamlit for a clean and interactive user interface.
- **Backend**: FastAPI for a high-performance API.
- **Database**: SQL (MySQL) for managing data.
- **Data Validation**: Pydantic for ensuring data integrity.
- **Logging**: Built-in logging for tracking application performance.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:  
   Use the command below to clone the repository to your local machine.
   ```bash
   https://github.com/saipreethikanr/Expense-Tracking-System-.git
   ```

2. **Navigate to the Project Directory**:  
   Change into the project directory.
   ```bash
   cd Expense-Tracking-System-
   ```

3. **Install Dependencies**:  
   Use pip to install the required Python packages.
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:  
   Ensure that your SQL database is running. Update the database configuration in the `config.py` file.

5. **Run the Application**:  
   Start the FastAPI server and the Streamlit app.
   ```bash
   uvicorn main:app --reload
   streamlit run app.py
   ```

6. **Access the Application**:  
   Open your web browser and go to `http://localhost:8501` to view the Streamlit application.

## Usage

After setting up the application, you can start tracking your expenses. Here’s how to use the key features:

### Adding an Expense

1. Navigate to the "Add Expense" section.
2. Fill in the details such as amount, category, and date.
3. Click "Submit" to save the expense.

### Viewing Analytics

1. Go to the "Analytics" tab.
2. View your spending patterns through various visualizations.
3. Use filters to refine your data based on categories or dates.

### Managing Expenses

1. Access the "Manage Expenses" section.
2. You can edit or delete any existing expense records.




