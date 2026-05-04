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

```
====================================
         Welcome to FinTrack
   Your Personal Finance Tracker
              v1.0
====================================
```

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

```
====================================
       Thank you for using
             FinTrack
          See you soon!
====================================
```

---

## How to Use the Program

1. Install dependencies: pip install gspread google-auth
2. Place your `creds.json` file in the project folder.
3. Run the program: python3 run.py

- User needs to type in the python3 run.py command in the Terminal or Heroku console
- When the program starts, users see:

Starting FinTrack ... 

- The Welcome banner is displayed.

```
====================================
         Welcome to FinTrack
   Your Personal Finance Tracker
              v1.0
====================================
```
- The main menu is displayed:
1. Add Transaction
2. View Transactions
3. View Summary
4. Exit

Users interact by entering the number of the desired option.


## Technologies Used

- Python 3  
- Google Sheets  
- gspread library  
- Google Cloud Service Account
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- oauth2client

---

## How the Code Works

The program connects to a Google Sheet named **FinTrack** using a service
account. It reads and writes data to the **Transactions** worksheet.

The code is structured into small, easy-to-understand functions:

- `clear_screen()` – Clear the terminal screen.
- `loading_animation(message="Loading")` - Display a simple loading animation with a custom message. Shows the message with 1, 2, and 3 dots, then clears the screen.
- `add_transaction()` – adds a new row to the Fintrack Google Sheets 
- `view_transactions()` – Display all transactions stored in the 'transactions' worksheet 
- `add_transaction()` – adds a new row  
- `view_summary()` – Displays a summary of all transactions stored in the "transactions" worksheet.  
- `main_menu()` – Displays the main menu, handles user choices and runs the program loop.

I focused on clarity and readability rather than complexity.

---

## Flowchart

The program follows this simple flow:

The FinTrack program follows a simple, linear flow:

```
[Start]
   ↓
Display Welcome Banner
   ↓
Display Main Menu
   ↓
User Choice
   ↓
 ┌─────────────────────────────────────────────┐
 │ If "1" → Add Transaction → Back to Menu     │
 │ If "2" → View Transactions → Back to Menu   │
 │ If "3" → View Summary → Back to Menu        │
 │ If "4" → Show Exit Banner → End Program     │
 │ Else → Show Error → Back to Menu            │
 └─────────────────────────────────────────────┘
```
This flow ensures the program is easy to use and follows a clear structure.  

Insert flowchart image in here

---


## Data Model
FinTrack uses a Google Sheet as its database.

Each row contains:

| Column | Field |
| --- | --- |
| A | Date |
| B | Description |
| C | Amount |
| D | Type |
| E | Category |

The sheet is accessed using:

gspread

google.oauth2.service_account

## Technologies Used

- Python 3

- Google Sheets API

- gspread

- Heroku

- VS Code Terminal

- Git & GitHub

## Testing

All testing is documented in TESTING.md.

Testing includes:

- manual feature testing

- input validation

- Google Sheets integration

- Heroku deployment testing

- PEP8 validation

- bug fixes
Heroku Deployment Steps

The project passed the CI Python Linter with zero errors.

## Deployment

### Heroku Deployment Steps

1. Create a new Heroku app
2. Add buildpacks:
       - heroku/python
3. Add required files:

        - requirements.txt
         - Procfile
   - runtime.txt

4. Push code to GitHub
5. In Heroku → Deploy tab → Manual Deploy → Deploy Branch
6. App builds and runs automatically

### Environment Variables
Add the following config var:
CREDS = <your service account JSON>

## Credits 

- Code Institute template for Google Sheets API setup
- Love Sandwiches-Esential  Walkthrough Project for project structure guidance and coding.
- Google Sheets API documentation
- spread documentation  
  

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
- Export summary to PDF
- Add monthly charts
- Add a login system
- Add categories dashboard


## 
---


