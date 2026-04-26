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
# View Transactions 
# -----------------------------
def view_transactions():
    """Print all transactions in a simple list."""

    # Print a header so the user knows what section they are viewing
    print("\n--- All Transactions ---\n")

# Call the load_transactions() function to get all rows from the Google Sheet
    transactions = transactions_ws.get_all_records()

 # If the list is empty, it means there are no transactions stored yet
    if not transactions:
        print("No transactions found.")
        return # Exit the function early because there is nothing to display

 # Loop through each transaction (each item is a dictionary)
    for t in transactions:
         # Print each field in a readable format
        # The keys must match the column names in the FinTrack Google Sheet
        print(f"{t['Date']} | {t['Description']} | {t['Amount']} | {t['Type']} | {t['Category']}")

# Print a footer line to make the output look clean
    print("\n-------------------------\n")

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

def view_summary():
    """Display a summary of all transactions stored in transactions/FinTrack Google Sheets."""

    print("\n--- Summary of Transactions ---\n")

    # Get all rows from the Google Sheets 'transactions' worksheet.
    # Each row contains: [date, description, amount, type, category]
    rows = transactions_ws.get_all_values()

    # If there are no transactions (only header row), inform the user.
    if len(rows) <= 1:
        print("No transactions found.")
        return

if __name__ == "__main__":
    print("TEST: Running main block")
    view_summary()


# -----------------------------
# TEMPORARY TEST BLOCK
# -----------------------------
if __name__ == "__main__":
    add_transaction()

# -----------------------------
# Print to confirm everything works
# -----------------------------

