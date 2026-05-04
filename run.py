import gspread
from google.oauth2.service_account import Credentials
import os
import time

# -----------------------------
# Google Sheets API Setup
# -----------------------------
# Permissions needed to access Google Sheets

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
# Load credentials from your JSON file
CREDS = Credentials.from_service_account_file("creds.json")

# Apply the permissions to the credentials
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Create a client to access Google Sheet
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# -----------------------------
# Open the FinTrack Google Sheet
# -----------------------------
SHEET = GSPREAD_CLIENT.open("FinTrack")

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

# ----------------------------------------------------
# Clear screen and loading animation functions
# ----------------------------------------------------


def clear_screen():
    """
    Clear the terminal screen.
    Works on Windows, macOS, Linux, and Heroku.
    """
    # Use the operating system's built‑in clear command.
    # On Windows the command is "cls", on macOS/Linux/Heroku it is "clear".
    # os.name returns "nt" on Windows, so we choose the correct command.
    os.system("cls" if os.name == "nt" else "clear")


def loading_animation(message="Loading"):
    """
    Display a simple loading animation with a custom message.
    Shows the message with 1, 2, and 3 dots, then clears the screen.
    """
    # Loop three times to create three animation steps.
    for i in range(3):

        # Print the message followed by a growing number of dots.
        # (i + 1) ensures the dots go: 1 dot → 2 dots → 3 dots.
        print(f"{message}{'.' * (i + 1)}")

        # Pause for 1.0 seconds so the animation is visible to the user.
        time.sleep(1.0)

        # Clear the screen after each step to create the animation effect.
        clear_screen()


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
    # This can be anything the user wants (e.g.,Food,Rent,Salary,Transport).
    # No strict validation here because categories can vary widely.
    category = input("Enter category: ").strip()

    # Prepare the new transaction row in the correct column order.
    # Must match the 'transactions' worksheet layout.

    new_row = [date, description, amount, t_type, category]

    # Append the new row to the Google Sheets 'transactions' worksheet.
    # This saves the transaction permanently in the'transactions' worsheet.
    transactions_ws.append_row(new_row)

    # Confirm to the user that the transaction was added successfully.
    print("\nTransaction added successfully!\n")

# -----------------------------
# View Transactions
# -----------------------------


def view_transactions():
    # Display all transactions stored in the 'transactions' worksheet.
    # Print a blank line and a header.
    print("\n--- All Transactions ---\n")

    # Get all rows from the Google Sheets as a list of lists
    rows = transactions_ws.get_all_values()

    # If only the header exists, there are no transactions
    if len(rows) <= 1:
        print("No transactions found.")
        return  # Exit early because there is nothing to display

    # Print the header row in a clean table formatted way
    # Get the first row (index 0) from the sheet; it contains the column names.
    header = rows[0]
    # Print each column name in fixed width so the table stays aligned.
    # {header[0]:<12}  → left-align the "Date" column in a 12-character space
    # {header[1]:<20}  → left-align "Description" in a 20-character space
    # {header[2]:<10}  → left-align "Amount" in a 10-character space
    # {header[3]:<10}  → left-align "Type" in a 10-character space
    # {header[4]:<15}  → left-align "Category" in a 15-character space
    # The "|" characters visually separate the columns like a table.
    # Print header columns with fixed widths for alignment.
    print(
        f"{header[0]:<12} | {header[1]:<20} | {header[2]:<10} | "
        f"{header[3]:<10} | {header[4]:<15}"
        )

    # Print a horizontal line made of 75 dashes.
    # Creates a separator between the header and the transaction rows.

    print("-" * 75)

    # Loop through rows (skip header at index 0) and print each transaction.

    for row in rows[1:]:
        # Extract each column from the row for readability
        date = row[0]
        description = row[1]
        amount = row[2]
        t_type = row[3]
        category = row[4]
        # Print a formatted transaction row in an aligned table view.
        # Print the transaction row using the header's fixed-width format.
        # f"{date:<12} = inserts the date and left-aligns it in 12 characters.
        # {description:<20}  inserts description left‑aligned in 20‑characters.
        # €{amount:<9} = prints € and left-aligns the amount in a 9-char field.
        # {t_type:<10} = prints the transaction type left‑aligned in 10 chars.
        # {category:<15}" = prints the category left‑aligned in 15 chars.
        # | = a visual separator between columns, like a table.
        print(
            f"{date:<12} | {description:<20} | €{amount:<9} | "
            f"{t_type:<10} | {category:<15}"
        )

        print()  # Print blank line at the end

# Run view_transactions only when this file is executed directly.


def view_summary():
    # Display a summary of all transactions stored in transactions worksheet.

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
        amount = float(row[2])  # Amount is in column 3, convert it to a float.
        t_type = row[3]  # Type (Income/Expense) is in column 4

        if t_type == "Income":
            total_income = total_income + amount  # Add to total income.
            income_count += 1  # Count income transactions
        elif t_type == "Expense":
            total_expense = total_expense + amount  # Add to total expenses.
            expense_count += 1  # Count expense transactions
            expense_values.append(amount)  # Save expense for later calc

    # Calculate the net balance (Income - Expense).
    net_balance = total_income - total_expense

    # Total number of transactions recorded (all rows except header).
    total_transactions = len(data_rows)

    # Dictionary to store total spending per category.
    # Calculate which category has the highest total spending.
    # We only consider Expense rows for this calculation.
    category_totals = {}
    # Loop through transactions to accumulate expense totals per category.

    for row in data_rows:
        amount = float(row[2])  # Amount value from the row/"Amount" column.
        t_type = row[3]  # Transaction type (Income/Expense) from the row.
        category = row[4]  # "Category" column.

        if t_type == "Expense":
            # Add amount to the category total
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    # ---------------------------------------------------------
    # FULLY ALIGNED SUMMARY OUTPUT (using f‑strings)
    # ---------------------------------------------------------

    print("\n=== Financial Summary ===\n")

    # Print income, expense, and net balance with aligned labels.
    print(f"{'Total Income:':25} €{total_income:,.2f}")
    print(f"{'Total Expense:':25} €{total_expense:,.2f}")
    print(f"{'Net Balance:':25} €{net_balance:,.2f}\n")

    # Print transaction counts with aligned labels.
    print(f"{'Number of Transactions:':25} {total_transactions}")
    print(f"{'Income Count:':25} {income_count}")
    print(f"{'Expense Count:':25} {expense_count}")

    # If there are any expenses, calculate average expense
    if expense_values:
        avg_expense = sum(expense_values) / len(expense_values)
        # Highest single expense.
        highest_expense = max(expense_values)
        print(f"{'Average Expense:':25} €{avg_expense:,.2f}")
        print(f"{'Highest Expense:':25} €{highest_expense:,.2f}")

    else:
        # If no expenses exist, show N/A for these fields.
        print(f"{'Average Expense:':25} N/A")
        print(f"{'Highest Expense:':25} N/A")

    print()  # Blank line for spacing

    # If there are any expenses, find the category with the highest total.
    if category_totals:
        # Find the category with the largest total expense.
        top_category = max(category_totals, key=category_totals.get)
        top_amount = category_totals[top_category]  # Total spent in that cat.
        print(f"{'Top Spending Category:':25} {top_category} "
              f"(€{top_amount:,.2f})\n")
    else:
        # If no expenses exist, no category can be ranked.
        print(f"{'Top Spending Category:':25} N/A\n")


def main_menu():
    """Display the main menu and handle user choices."""

    # Clear the terminal screen before showing anything.
    # This ensures the program starts with a clean, uncluttered interface.
    clear_screen()

    # Show a short loading animation before displaying the welcome banner.
    # This gives the effect of the program "starting up" like a real app.
    loading_animation("Starting FinTrack")

    # Welcome banner (prints once when the program starts)
    print("\n====================================")
    print("         Welcome to FinTrack")
    print("   Your Personal Finance Tracker")
    print("              v1.0")
    print("====================================\n")
    # Start an infinite loop to keep showing the menu until the user exits.

    while True:
        # Print the main menu options for the user
        print("\n=== FinTrack Main Menu ===")
        print("1. Add a new transaction")
        print("2. View all transactions")
        print("3. View summary")
        print("4. Exit")

        # Ask the user to enter a menu option and remove any extra spaces
        choice = input("Enter your choice (1-4): ").strip()

        # If the user selects option 1, call the function to add a new trans.
        if choice == "1":
            # Clear the screen before showing the add transaction form.
            clear_screen()
            add_transaction()

        # If the user selects option 2, call the function to display all trans.
        elif choice == "2":
            # Clear the screen before displaying the transaction table.
            clear_screen()
            view_transactions()

        # If the user selects option 3, show the financial summary report.

        elif choice == "3":
            # Clear the screen before displaying the summary report.
            clear_screen()
            view_summary()

        # If the user selects option 4, exit the loop and end/exit the program.
        elif choice == "4":
            # Clear the screen before showing the goodbye banner.
            clear_screen()

            # Goodbye banner shown when the user exits the program.
            print("====================================")
            print("       Thank you for using")
            print("             FinTrack")
            print("          See you soon!")
            print("====================================\n")

            break  # Break stops the while loop and ends the program

        # If the user enters invalid menu choices, show an error message
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Run the main menu when the file is executed directly.

if __name__ == "__main__":
    main_menu()
