# Expense Tracker: A Comprehensive Expense Management System 💰

![Expense Tracker](https://img.shields.io/badge/Expense_Tracker-Ready-brightgreen)  
[![Releases](https://img.shields.io/badge/Releases-Click_here-brightorange)](https://github.com/chantipoloju/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/releases)

Welcome to the **Expense Tracker** project! This application helps you manage your daily expenses effectively. It combines a user-friendly Streamlit frontend, a robust FastAPI backend, and an SQL database for seamless data handling. 

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

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
   git clone https://github.com/chantipoloju/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic.git
   ```

2. **Navigate to the Project Directory**:  
   Change into the project directory.
   ```bash
   cd codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic
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

## Contributing

We welcome contributions to enhance the project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

- **GitHub**: [chantipoloju](https://github.com/chantipoloju)
- **Email**: your-email@example.com

## Releases

You can find the latest releases of the project [here](https://github.com/chantipoloju/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/releases). Download the necessary files and execute them to get started.

Thank you for checking out the Expense Tracker project! We hope you find it useful for managing your finances. Happy tracking!