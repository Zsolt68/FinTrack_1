# FinTrack – Personal Finance Tracker

FinTrack is a simple Python application that helps users track their personal
income and spending. All data is stored in a Google Sheets document, and the program can:

- Add a new transaction
- View all transactions
- View a simple financial summary

This project was intentionally kept simple because it is my first Python
application. My goal was to demonstrate a clear understanding of Python basics,
functions, loops, input validation, and working with external data using the
gspread library.

## 1. Project Overview
FinTrack is a lightweight, terminal‑based finance tracker designed for users who want a simple way to:

- log daily income and expenses

- store data in the cloud

- view transaction history

- generate financial summaries

- run the program anywhere (local or Heroku)

The goal of the project is to demonstrate:

- Python programming

- data validation

- Google Sheets API integration

- modular code structure

 - deployment to Heroku

- clean documentation and testing
---

## Features

### 1. Welcome banner

Displays a clean welcome message when the program starts.

====================================
         Welcome to FinTrack
   Your Personal Finance Tracker
              v1.0
====================================

### 2. View Transactions
Displays all transactions stored in the Google Sheet in a simple list format.

### 3. Add a New Transaction
Users can add a new income or expense with:
- Date  
- Description  
- Amount  
- Type (Income/Expense)  
- Category  

The new transaction or data is added directly to the FinTrack Google Sheet.

### 4. View All Transactions

Displays all stored transactions in a clean, aligned table:
- Date  
- Description  
- Amount  
- Type  
- Category  

This gives the user a quick overview of their financial situation.

### 5. Input Validation

Prevents invalid entries such as:
- non‑numeric amounts
- invalid transaction types
- empty fields

### 6. Loading Animation & Screen Clear

Improves user experience and readability.

### 6. Loading Animation & Screen Clear

Displays a clean exit message when the program ends.

### 7. Exit Banner

Displays a clean exit message when the program ends.

====================================
       Thank you for using
             FinTrack
          See you soon!
====================================

---

## Technologies Used

- Python 3  
- Google Sheets  
- gspread library  
- Google Cloud Service Account  

---

## How the Code Works

The program connects to a Google Sheet named **FinTrack** using a service
account. It reads and writes data to the **Transactions** worksheet.

The code is structured into small, easy-to-understand functions:

- `load_transactions()` – loads all data  
- `view_transactions()` – prints transactions  
- `add_transaction()` – adds a new row  
- `view_summary()` – calculates totals  
- `show_menu()` – displays the menu  
- `main()` – runs the program loop  

I focused on clarity and readability rather than complexity.

---

## Flowchart

The program follows this simple flow:

The FinTrack program follows a simple, linear flow:

1. Start the program
2. Load transactions from Google Sheets
3. Display main menu
4. User selects an option:
   - View Transactions → Display all rows
   - Add Transaction → Ask for input → Save to sheet
   - View Summary → Calculate totals → Display results
   - Exit → End program
5. After completing an action, return to the menu
6. Program ends when the user chooses Exit

This flow ensures the program is easy to use and follows a clear structure.  

Insert flowchart image in here

---

## How to Run

1. Install dependencies: pip install gspread google-auth
2. Place your `creds.json` file in the project folder.
3. Run the program: python3 run.py


---

## Future Enhancements

- Add filtering options (by category, date, or type)
- Add editing or deleting existing transactions
- Add a Categories management menu
- Write summary results back into the Summary worksheet
- Add charts or graphs for visual insights
- Add data validation directly in Google Sheets
- Add a Logs worksheet to track user actions
- Add monthly or yearly reports

---

## Credits

- Python documentation  
- gspread documentation  
- Code Institute template for Google Sheets API setup and "Love Sandwiches" Walkthrough Project.

