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


# -----------------------------
# Print to confirm everything works
# -----------------------------
print("TRANSACTIONS:")
print(transactions_data)

print("\nCATEGORIES:")
print(categories_data)

print("\nSUMMARY:")
print(summary_data)

print("\nSETTINGS:")
print(settings_data)
