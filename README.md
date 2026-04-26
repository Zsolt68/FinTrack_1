![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# FinTrack – Personal Finance Tracker

FinTrack is a simple Python application that helps users track their personal
income and spending. All data is stored in a Google Sheets document, and the program can:

- View all transactions
- Add a new transaction
- View a simple financial summary

This project was intentionally kept simple because it is my first Python
application. My goal was to demonstrate a clear understanding of Python basics,
functions, loops, input validation, and working with external data using the
gspread library.

---

## Features

### 1. View Transactions
Displays all transactions stored in the Google Sheet in a simple list format.

### 2. Add Transaction
Allows the user to enter:
- Date  
- Description  
- Amount  
- Type (Debit or Credit)  
- Category  

The new transaction is added directly to the Google Sheet.

### 3. View Summary
Calculates:
- Total Income  
- Total Spending  
- Net Balance  

This gives the user a quick overview of their financial situation.

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

