# Testing
This document outlines all testing performed on the FinTrack application, including manual testing, validation checks, and deployment verification.

## 1. Manual Testing
All features were manually tested in the terminal (Gitpod) and on Heroku.
Each test case includes the expected result and the actual result.

### 1.1 Main Menu Navigation

| Test | Action | Expected Result | Actual Result | Pass |
| --- | --- | --- | --- | --- |
| 1 | Start app | Welcome banner + main menu displayed | As expected | ✔ |
| 2 | Enter ``1`` | Add Transaction form appears | As expected | ✔ |
| 3 | Enter ``2`` | All transactions table displayed | As expected | ✔ |
| 4 | Enter ``3`` | Summary report displayed | As expected | ✔ |
| 5 | Enter ``4`` | Exit banner displayed and program ends | As expected | ✔ |
| 6 | Enter invalid input (e.g., ``abc``) | Error message shown | As expected | ✔ |


## 2. Add Transaction Feature
Test	Input	Expected Result	Actual Result	Pass
1	Valid date	Accepted	As expected	✔
2	Valid description	Accepted	As expected	✔
3	Valid amount (12.50)	Saved as float	As expected	✔
4	Invalid amount (abc)	Error message + return to menu	As expected	✔
5	Type = Income	Accepted	As expected	✔
6	Type = Expense	Accepted	As expected	✔
7	Invalid type (Food)	Error message	As expected	✔
8	Category text	Accepted	As expected	✔
9	Entire row appended to Google Sheets	Row appears in sheet	✔


## 3. View Transactions Feature
Test	Action	Expected Result	Actual Result	Pass
1	Display table	Aligned columns	As expected	✔
2	Long descriptions	Overflow allowed (expected)	As expected	✔
3	No transactions	“No transactions found”	As expected	✔
4	Currency formatting	€ symbol displayed	As expected	✔


## 4. Summary Report Feature
Test	Action	Expected Result	Actual Result	Pass
1	Calculate totals	Correct totals displayed	✔
2	Calculate net balance	Income − Expense	✔
3	Count transactions	Correct count	✔
4	Average expense	Correct calculation	✔
5	Highest expense	Correct value	✔
6	Top spending category	Correct category	✔
7	No expenses	Show “N/A”	✔


## 5. Input Validation
Input	Expected Result	Actual Result	Pass
Empty input	Prompt again or error	✔
Spaces only	Stripped and validated	✔
Lowercase “income”	Converted to “Income”	✔
Lowercase “expense”	Converted to “Expense”	✔
Invalid menu choice	Error message	✔


## 6. Heroku Deployment Testing
Test	Action	Expected Result	Actual Result	Pass
1	App loads	Welcome banner appears	✔
2	No auto‑running functions	No transactions shown on startup	✔
3	Menu works	All options functional	✔
4	Google Sheets connection	Data loads correctly	✔
5	Add transaction	Row appears in live sheet	✔
6	View transactions	Table displays correctly	✔
7	Summary	Calculations correct	✔


## 7. PEP8 / Linter Validation
The entire project was tested using the CI Python Linter.

File	Errors	Result
run.py	0	✔ Fully PEP8 compliant


## 8. Bugs Found & Fixes
### Bug 1 — App showed transactions before welcome banner
Cause: Duplicate entry point:

python
if __name__ == "__main__":
    view_transactions()
Fix: Removed the block so only main_menu() runs.

### Bug 2 — Long descriptions overflow table
Status: Expected behaviour.
Reason: Description column is fixed at 20 characters.
Decision: Left as‑is for readability.

### Bug 3 — Invalid amount caused crash
Fix: Wrapped conversion in try/except and returned safely.

## 9. Browser / Terminal Compatibility
Environment	Result
Gitpod terminal	✔ Fully functional
Heroku console	✔ Fully functional
Windows CMD	✔ Works
macOS Terminal	✔ Works
Linux Terminal	✔ Works
