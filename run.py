import gspread
from google.oauth2.service_account import Credentials

# -----------------------------
# Google Sheets API Setup
# -----------------------------
# Permissions needed to access Google Sheets

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# Load credentials from your JSON file
CREDS = Credentials.from_service_account_file('creds.json')

# Apply the permissions to the credentials
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Create a client to access Google Sheet
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# -----------------------------
# Open the FinTrack Google Sheet
# -----------------------------
SHEET = GSPREAD_CLIENT.open('FinTrack')

# -----------------------------
# Load each worksheet
# -----------------------------

transactions_ws = SHEET.worksheet("transactions")
categories_ws = SHEET.worksheet("categories")
summary_ws = SHEET.worksheet("summary")
settings_ws = SHEET.worksheet("settings")

# -----------------------------
# Get data from each worksheet
# -----------------------------
transactions_data = transactions_ws.get_all_records()
categories_data = categories_ws.get_all_records()
summary_data = summary_ws.get_all_records()
settings_data = settings_ws.get_all_records()


# -----------------------------
# Add a New Transaction
# -----------------------------

def add_transaction():
    """Ask the user for transaction details and save them to Google Sheets."""

    print("\n--- Add New Transaction ---\n")

 # Ask the user for the date of the transaction
    date = input("Enter the date (DD/MM/YYYY): ").strip()

    # Ask the user for a short description of the transaction
    description = input("Enter a description: ").strip()

    # Ask the user for the amount and validate it
    amount_input = input("Enter the amount: ").strip()

    # Basic validation: check if the amount is a number
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return  # Stop the function if invalid input is given

 # Ask the user whether this is income or spending
    t_type = input("Enter type (Income/Expense): ").strip().capitalize()

    # Validate the type
    if t_type not in ["Income", "Expense"]:
        print("Invalid type. Please enter 'Income' or 'Expense'.")
        return


    # Ask the user for the transaction category.
    # This can be anything the user wants (e.g., Food, Rent, Salary, Transport).
    # No strict validation here because categories can vary widely.
    category = input("Enter category: ").strip()

    # Prepare the new transaction row in the correct order for the FinTrack Google Sheets.
    # The order must match the columns in the 'transactions' worksheet.
    new_row = [date, description, amount, t_type, category]

    # Append the new row to the Google Sheets 'transactions' worksheet.
    # This saves the transaction permanently in the'transactions'/FinTrack Google Sheets.
    transactions_ws.append_row(new_row)

    # Confirm to the user that the transaction was added successfully.
    print("\nTransaction added successfully!\n")

    # -----------------------------
# View Transactions 
# -----------------------------
def view_transactions():
    """Display all transactions stored in the Google Sheets 'transactions' worksheet."""

# Print a blank line and a header so the user knows what section they are viewing
    print("\n--- All Transactions ---\n")

    # Get all rows from the Google Sheets as a list of lists
    rows = transactions_ws.get_all_values()

    # If only the header exists, there are no transactions
    if len(rows) <= 1:
        print("No transactions found.")
        return # Exit early because there is nothing to display

    # Print the header row in a clean table formatted way
    # Takes the first row from the transaction worksheet (index 0), which contains the column names
    header = rows[0]
    # Print each column name in a fixed-width format so the table looks aligned.
# {header[0]:<12}  → left-align the "Date" column in a 12-character space
# {header[1]:<20}  → left-align "Description" in a 20-character space
# {header[2]:<10}  → left-align "Amount" in a 10-character space
# {header[3]:<10}  → left-align "Type" in a 10-character space
# {header[4]:<15}  → left-align "Category" in a 15-character space
# The "|" characters visually separate the columns like a table.
    print(f"{header[0]:<12} | {header[1]:<20} | {header[2]:<10} | {header[3]:<10} | {header[4]:<15}")

# Print a horizontal line made of 75 dashes.
# This creates a clean visual separator between the header and the transaction rows.
    print("-" * 75)

    # Loop through each transaction row (skipping the header at index 0) and print each transaction row
    for row in rows[1:]:
    # Extract each column from the row for readability  
        date = row[0]
        description = row[1]
        amount = row[2]
        t_type = row[3]
        category = row[4]
# Prints a formatted transaction row in a clean, aligned table format to the screen.
# Prints the transaction row with the same fixed-width formatting as the header.
# f"{date:<12} = insert the value of date and left‑align the text inside a 12‑character wide space.
# {description:<20} = insert description and left‑align in a 20‑character space.
# €{amount:<9} = print a euro symbol before the amount and left‑align the amount in a 9‑character space.
# {t_type:<10} = insert the transaction type (Income or Expense) and left‑align the amount in a 10‑character space.Gives it a fixed width so the next column lines up.
# {category:<15}" = insert the category name and left‑align the amount in a 15‑character space.
# | = a visual separator between columns, like a table.
        print(f"{date:<12} | {description:<20} | €{amount:<9} | {t_type:<10} | {category:<15}")

    print()  # Print blank line at the end

if __name__ == "__main__":
    view_transactions()

def view_summary():
    """Display a summary of all transactions stored in transactions/FinTrack Google Sheets."""

    print("\n=== Financial Summary ===\n")

    # Get all rows from the Google Sheets 'transactions' worksheet.
    # Each row contains: [date, description, amount, type, category]
    rows = transactions_ws.get_all_values()

    # If there are no transactions (only header row), inform the user.
    if len(rows) <= 1:
        print("No transactions found.")
        return

    # Remove the header row so we only process actual transactions.
    data_rows = rows[1:]

    # Initialize totals for income and expenses.
    total_income = 0
    total_expense = 0

    # Counters for number of income and expense transactions.
    income_count = 0
    expense_count = 0

    # List to store all expense amounts (used for average + highest expense).
    expense_values = []


    # Loop through each transaction row and accumulate totals.
    for row in data_rows:
        amount = float(row[2])     # Amount is in column 3
        t_type = row[3]            # Type (Income/Expense) is in column 4

        if t_type == "Income":
            total_income = total_income + amount
            income_count += 1       # Count income transactions
        elif t_type == "Expense":
            total_expense = total_expense + amount
            expense_count += 1     # Count expense transactions
            expense_values.append(amount)  # Store for later calculations   

    # Calculate the net balance (Income - Expense).
    net_balance = total_income - total_expense

    # Display the calculated summary to the user.
    print(f"Total Income: €{total_income:.2f}")
    print(f"Total Expense: €{total_expense:.2f}")
    print(f"Net Balance: €{net_balance:.2f}\n")

# --- Additional Summary Metrics ---

    # Total number of transactions recorded.
    total_transactions = len(data_rows)
    print(f"Number of Transactions: {total_transactions}")

    
    # Calculate which category has the highest total spending.
    # We only consider Expense rows for this calculation.
    category_totals = {}

    for row in data_rows:
        amount = float(row[2])
        t_type = row[3]
        category = row[4]

        if t_type == "Expense":
        # Add amount to the category total
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount


# If there are any expenses, find the category with the highest total.
    if category_totals:
        top_category = max(category_totals, key=category_totals.get)
        top_amount = category_totals[top_category]
        print(f"Top Spending Category: {top_category} (€{top_amount:.2f})\n")
    else:
        print("No expenses recorded, so no top category.\n")
        
def main_menu():
    """Display the main menu and handle user choices."""
    
    # Start an infinite loop so the menu keeps showing until the user chooses to exit
    while True:
        # Print the main menu options for the user
        print("\n=== FinTrack Main Menu ===")
        print("1. Add a new transaction")
        print("2. View all transactions")
        print("3. View summary")
        print("4. Exit")

        # Ask the user to enter a menu option and remove any extra spaces
        choice = input("Enter your choice (1-4): ").strip()

        # If the user selects option 1, call the function to add a new transaction
        if choice == "1":
            add_transaction()

        # If the user selects option 2, call the function to display all transactions
        elif choice == "2":
            view_transactions()

        # If the user selects option 3, call the function to show the summary report
        elif choice == "3":
            view_summary()

        # If the user selects option 4, exit the loop and end the program
        elif choice == "4":
            print("Exiting FinTrack. Goodbye!")
            break  # Break stops the while loop and ends the program

        # If the user enters anything else, show an error message
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def main_menu():
    """Display the main menu and handle user choices."""
    
    # Start an infinite loop so the menu keeps showing until the user chooses to exit
    while True:
        # Print the main menu options for the user
        print("\n=== FinTrack Main Menu ===")
        print("1. Add a new transaction")
        print("2. View all transactions")
        print("3. View summary")
        print("4. Exit")

        # Ask the user to enter a menu option and remove any extra spaces
        choice = input("Enter your choice (1-4): ").strip()
        
        # If the user selects option 1, call the function to add a new transaction
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Exiting FinTrack. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        


# -----------------------------
# TEMPORARY TEST BLOCK
# -----------------------------
if __name__ == "__main__":
     main_menu()



