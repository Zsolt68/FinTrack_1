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

| Test | Input                                | Expected Result                     | Actual Result | Pass |
|------|---------------------------------------|-------------------------------------|---------------|------|
| 1    | Valid date                            | Accepted                            | As expected   | ✔    |
| 2    | Valid description                     | Accepted                            | As expected   | ✔    |
| 3    | Valid amount (`12.50`)                | Saved as float                      | As expected   | ✔    |
| 4    | Invalid amount (`abc`)                | Error message + return to menu      | As expected   | ✔    |
| 5    | Type = `Income`                       | Accepted                            | As expected   | ✔    |
| 6    | Type = `Expense`                      | Accepted                            | As expected   | ✔    |
| 7    | Invalid type (`Food`)                 | Error message                       | As expected   | ✔    |
| 8    | Category text                         | Accepted                            | As expected   | ✔    |
| 9    | Entire row appended to Google Sheets  | Row appears in sheet                | ✔             | ✔    |



## 3. View Transactions Feature

| Test | Action | Expected Result | Actual Result | Pass |
| --- | --- | --- | --- | --- |
| 1 | Display table | Aligned columns | As expected | ✔ |
| 2 | Long descriptions | Overflow allowed (expected) | As expected | ✔ |
| 3 | No transactions | “No transactions found” | As expected | ✔ |
| 4 | Currency formatting | ``€`` symbol displayed | As expected | ✔ |


## 4. Summary Report Feature

| Test | Action                 | Expected Result        | Actual Result | Pass |
|------|------------------------|------------------------|----------------|------|
| 1    | Calculate totals       | Correct totals displayed | ✔            | ✔    |
| 2    | Calculate net balance  | Income − Expense       | ✔            | ✔    |
| 3    | Count transactions     | Correct count          | ✔            | ✔    |
| 4    | Average expense        | Correct calculation    | ✔            | ✔    |
| 5    | Highest expense        | Correct value          | ✔            | ✔    |
| 6    | Top spending category  | Correct category       | ✔            | ✔    |
| 7    | No expenses            | Show “N/A”             | ✔            | ✔    |



## 5. Input Validation

| Input | Expected Result | Actual Result | Pass |
| --- | --- | --- | --- |
| Empty input | Prompt again or error | ✔ |
| Spaces only | Stripped and validated | ✔ |
| Lowercase “income” | Converted to “Income” | ✔ |
| Lowercase “expense” | Converted to “Expense” | ✔ |
| Invalid menu choice | Error message | ✔ |


## 6. Heroku Deployment Testing

| Test | Action | Expected Result | Actual Result | Pass |
| --- | --- | --- | --- | --- |
| 1 | App loads | Welcome banner appears | ✔ |
| 2 | No auto‑running functions | No transactions shown on startup | ✔ |
| 3 | Menu works | All options functional | ✔ |
| 4 | Google Sheets connection | Data loads correctly | ✔ |
| 5 | Add transaction | Row appears in live sheet | ✔ |
| 6 | View transactions | Table displays correctly | ✔ |
| 7 | Summary | Calculations correct | ✔ |


## 7. PEP8 / Linter Validation
The entire project was tested using the CI Python Linter.

Linter Errors (Before Fixes)

| Line | Error Code | Description |
| --- | --- | --- |
| 51 | E302 | expected 2 blank lines, found 1 |
| 115 | E501 | line too long (80 > 79 characters) |
| 119 | E501 | line too long (90 > 79 characters) |
| 124 | E501 | line too long (89 > 79 characters) |
| 128 | W291 | trailing whitespace |
| 133 | E302 | expected 2 blank lines, found 1 |
| 134 | E501 | line too long (88 > 79 characters) |
| 136 | E501 | line too long (85 > 79 characters) |
| 148 | E501 | line too long (99 > 79 characters) |
| 150 | E501 | line too long (80 > 79 characters) |
| 158 | E501 | line too long (98 > 79 characters) |
| 162 | E501 | line too long (88 > 79 characters) |
| 165 | E501 | line too long (103 > 79 characters) |
| 173 | E501 | line too long (92 > 79 characters) |
| 174 | E501 | line too long (88 > 79 characters) |
| 175 | E501 | line too long (107 > 79 characters) |
| 176 | E501 | line too long (88 > 79 characters) |
| 177 | E501 | line too long (112 > 79 characters) |
| 178 | E501 | line too long (174 > 79 characters) |
| 179 | E501 | line too long (103 > 79 characters) |
| 182 | E501 | line too long (92 > 79 characters) |
| 193 | E501 | line too long (94 > 79 characters) |
| 226 | E261 | at least two spaces before inline comment |
| 229 | E261 | at least two spaces before inline comment |
| 231 | E501 | line too long (81 > 79 characters) |
| 243 | W293 | blank line contains whitespace |
| 244 | E501 | line too long (85 > 79 characters) |
| 247 | E501 | line too long (88 > 79 characters) |
| 256 | W293 | blank line contains whitespace |
| 271 | W291 | trailing whitespace |
| 272 | W293 | blank line contains whitespace |
| 273 | W291 | trailing whitespace |
| 276 | W293 | blank line contains whitespace |
| 288 | W293 | blank line contains whitespace |
| 290 | E303 | too many blank lines (2) |
| 294 | E501 | line too long (83 > 79 characters) |
| 295 | E501 | line too long (85 > 79 characters) |
| 309 | E501 | line too long (81 > 79 characters) |
| 319 | W293 | blank line contains whitespace |
| 320 | E303 | too many blank lines (2) |
| 320 | E501 | line too long (85 > 79 characters) |
| 332 | E501 | line too long (83 > 79 characters) |
| 338 | E501 | line too long (86 > 79 characters) |
| 344 | E501 | line too long (95 > 79 characters) |
| 352 | E114 | indentation is not a multiple of 4 (comment) |
| 352 | E117 | over‑indented (comment) |
| 371 | E305 | expected 2 blank lines after function definition |

Linter Errors (After Fixes)

| File | Errors | Result |
| --- | --- | --- |
| run.py | 0 | ✔ All issues resolved — fully PEP8 compliant |

Summary Paragraph for TESTING.md
All files were tested using the CI Python Linter.
Initially, multiple issues were identified, including long lines (E501), missing or extra blank lines (E302, E305, E303), trailing whitespace (W291, W293), indentation issues (E114, E117), and inline comment spacing errors (E261).

Each issue was corrected through iterative cleanup, line‑length reduction, whitespace removal, and consistent formatting.

After applying all fixes, the project passed the CI Python Linter with zero errors, confirming full PEP8 compliance.

![PEP8](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen)

<p align="center">
  <img src="https://img.shields.io/badge/Code%20Style-PEP8-brightgreen" alt="PEP8 Badge">
</p>

## 8. Bugs Found & Fixes
### Bug 1 — App showed transactions before the welcome banner
Cause: Duplicate entry point:

python
if __name__ == "__main__":
    view_transactions()
Fix: Removed the block so only main_menu() runs.

### Bug 2 — Long descriptions overflow table
Status: Expected behaviour.
Reason: Description column is fixed at 20 characters.
Decision: Left as‑is for readability.

## 9. Browser / Terminal Compatibility

| Environment | Result |
| --- | --- |
| Visual Studio Code terminal | ✔ Fully functional |
| Heroku Terminal (web console) | ✔ Fully functional |
