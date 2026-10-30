# 🏦 Banking Management System

```{=html}
<p align="center">
```
`<strong>`{=html}A Python-based, menu-driven banking application built
with Object-Oriented Programming and core Python
concepts.`</strong>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white">`{=html}
`<img alt="Project" src="https://img.shields.io/badge/Project-Console%20Application-2ea44f">`{=html}
`<img alt="Storage" src="https://img.shields.io/badge/Storage-In%20Memory-orange">`{=html}
`<img alt="Purpose" src="https://img.shields.io/badge/Purpose-Learning-informational">`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 📌 About The Project

The **Banking Management System** is a beginner-friendly, menu-driven
Python console project. It demonstrates how common banking operations
can be organized using a class, methods, lists, dictionaries, loops,
conditional statements, `match-case`, Python standard-library modules,
and text-file handling.

Users can create accounts, deposit and withdraw money, calculate
interest, record loan details, generate account statements, view
customer records, and close accounts.

> ⚠️ **Educational project only:** This application is not connected to
> a real bank and is not suitable for handling real money or sensitive
> financial information.

## ✨ Features

  -----------------------------------------------------------------------
  Feature                             Description
  ----------------------------------- -----------------------------------
  🆕 Create Account                   Collects customer details and
                                      generates a customer ID and account
                                      number.

  💰 Deposit Amount                   Adds a deposit to the selected
                                      customer's account balance.

  💸 Withdraw Amount                  Deducts a withdrawal amount from
                                      the account balance.

  📈 Calculate Interest               Calculates interest according to
                                      the account type.

  🏦 Take Loan                        Collects loan details and
                                      calculates simple interest and
                                      total payable amount.

  🧾 Generate Statement               Creates a text file containing
                                      account information and recorded
                                      transactions.

  👤 Display Single Customer          Intended to show the details of one
                                      selected account.

  👥 Display All Customers            Displays customer records held
                                      during the current program session.

  🔒 Close Account                    Intended to remove an account after
                                      user confirmation.

  🚪 Exit                             Ends the application.
  -----------------------------------------------------------------------

## 🧰 Technologies & Python Concepts

-   🐍 **Python** --- primary programming language.
-   🧱 **Object-Oriented Programming (OOP)** --- banking operations are
    grouped inside the `BankManagement` class.
-   📚 **Lists and Dictionaries** --- store customer details, loan
    details, and transaction records.
-   🔁 **Loops** --- `for` and `while` loops search records and keep the
    menu running.
-   🔀 **Match-case** --- handles menu selections and account-type
    choices.
-   🧩 **Functions and Methods** --- each banking operation is organized
    into a separate method.
-   🆔 **UUID (`uuid`)** --- generates a customer ID using
    `uuid.uuid1()`.
-   🎲 **Random (`random`)** --- generates a 12-digit account number.
-   📅 **Date and Time (`datetime`)** --- records account opening and
    transaction timestamps.
-   📄 **File Handling** --- writes account statements to `.txt` files.
-   🖥️ **Console I/O** --- accepts user input and displays operation
    results.

The code imports `os`, but the supplied version does not currently use
it.

## 📂 Project Structure

``` text
Banking-Management-System/
│
├── banking.py
├── README.md
│
└── <account_number>_summary.txt
```

-   `banking.py` --- main Python application (use your actual Python
    filename).
-   `README.md` --- project documentation.
-   `<account_number>_summary.txt` --- statement file generated when the
    statement option is used.

## ⚙️ Requirements

-   Python **3.10 or later** because the project uses `match-case`.
-   Any Python editor or IDE, such as Visual Studio Code, PyCharm, or
    IDLE.
-   No third-party packages are required by the code shown.

> **Python version note:** The nested quotation marks in some f-strings
> may require Python 3.12 or later. For Python 3.10 or 3.11, use single
> quotes inside dictionary lookups, for example:
> `f"{data['customer_name']}"`.

## ▶️ Installation & Run

### 1. Get the project

Download the project folder or clone your GitHub repository:

``` bash
git clone <your-repository-url>
```

### 2. Open the project directory

``` bash
cd Banking-Management-System
```

### 3. Run the Python file

Replace `banking.py` with your actual filename if it is different.

``` bash
python banking.py
```

On Windows, this command may also work:

``` bash
py banking.py
```

## 🖥️ Application Menu

The program displays a menu similar to:

``` text
========== WELCOME TO BANKING MANAGEMENT SYSTEM ==========

1. Create an account
2. Deposit amount
3. Withdraw amount
4. Check interest
5. Take loan
6. Generate statement
7. Display single customer
8. Display all customers
9. Close account
10. Exit

Enter your choice:
```

Enter the number of the operation you want to perform.

## 🔍 How The Application Works

### 🆕 1. Create Account

The `create_new()` method asks the user for:

-   Customer name
-   City
-   Mobile number
-   Account type: Current or Savings
-   Opening balance

It then generates: - A customer ID using `uuid.uuid1()`. - A 12-digit
account number using `random.randint()`. - An opening timestamp using
`datetime.datetime.now()`.

The customer information is stored as a dictionary inside the `customer`
list. A separate empty `transaction` list is created for that account.

### 💰 2. Deposit Amount

The `deposit_am()` method asks for an account number, searches the
`customer` list, and adds the entered amount to the matching account's
`opening_balance`.

It also appends a transaction dictionary containing: - Transaction
type - Amount - Date and time

### 💸 3. Withdraw Amount

The `withdraw_am()` method searches for the account and subtracts the
entered withdrawal amount from its balance. It is intended to record the
transaction type, amount, and timestamp in the account's transaction
list.

**Current-code issue:** The supplied code records the withdrawal type as
`"deposit"`. Change it to `"withdraw"` so the transaction history is
accurate. The supplied code also does not check whether the withdrawal
amount exceeds the available balance.

### 📈 4. Calculate Interest

The `calculate_interest()` method uses the account type to select a
rate:

  Account Type     Rate in the supplied code
  -------------- ---------------------------
  Current                                 4%
  Savings                                 7%

Formula:

``` text
Interest = Current Balance × Rate
Updated Balance = Current Balance + Interest
```

These are example rates defined in the project code, not verified bank
interest rates. The method applies interest whenever the user selects
the option; it does not currently enforce a yearly schedule or add an
interest transaction to the transaction history.

### 🏦 5. Take Loan

The `taking_loan()` method asks for: - Loan amount - Loan interest
rate - Loan duration

It calculates simple interest:

``` text
Loan Interest = (Loan Amount × Interest Rate × Duration) / 100
Total Payable = Loan Amount + Loan Interest
```

The loan record is stored as a dictionary in the `customer_loan` list.
In the supplied code, loan information is stored separately and the loan
amount is not added to the customer's account balance.

### 🧾 6. Generate Statement

The `generate_statement()` method searches for the account and creates a
file named:

``` text
<account_number>_summary.txt
```

The file contains customer details and the transactions present in that
customer's `transaction` list.

The file is opened in **write mode (`"w"`)**: - If the file does not
exist, Python creates it. - If the file already exists, its old content
is cleared and replaced. - The method writes the current account
information and transaction history again.

This is appropriate when generating a fresh, complete statement. The
supplied version does not yet write loan details into the statement.

### 👤 7. Display Single Customer

The `display_SingleAccount()` method is intended to search by account
number and display only the matching customer's information.

**Current-code issues:** The method is missing `self`; after finding a
match, it loops through all customers instead of displaying only the
matched customer. It also accesses keys such as `balance`, `credit`,
`debit`, `loan`, and `interest`, which are not created in the account
dictionary. The balance key actually used by account creation is
`opening_balance`.

### 👥 8. Display All Customers

The `display_customer()` method is intended to loop through the
`customer` list and print every customer's information.

**Current-code issue:** It also refers to keys that are not present
(`balance`, `credit`, `debit`, `loan`, and `interest`). Use the existing
`opening_balance` key, and calculate credit/debit totals from
transaction history if those totals are required.

### 🔒 9. Close Account

The `close_ac()` method asks for an account number and confirmation
before removing the customer record.

**Current-code issue:** The comparison uses
`customer["customer_accountnumber"]`, but `customer` is a list of
dictionaries. The account number should be compared against each
dictionary, for example `data["customer_accountnumber"]`.

## 💾 Data Storage & Important Limitation

The supplied version stores records in two in-memory lists:

``` python
customer = []
customer_loan = []
```

This means: - Customer and loan records are available only while the
program is running. - When the program exits, those records are lost. -
Generated statement text files remain on disk, but the program does not
reload customer records from them at startup.

**Suggested next step:** Add JSON file handling to save and load
customer, loan, and transaction records between program runs.

## 🛠️ Recommended Improvements

The following checklist identifies useful next steps for improving the
supplied code:

-   [ ] Correct the withdrawal transaction type to `"withdraw"`.
-   [ ] Prevent withdrawals greater than the available balance.
-   [ ] Show "account not found" only after the full customer list has
    been searched.
-   [ ] Add `self` to `display_SingleAccount()` and display only the
    matched account.
-   [ ] Replace non-existent dictionary keys in both display methods.
-   [ ] Correct the account lookup in `close_ac()` and handle both Yes
    and No choices.
-   [ ] Validate mobile number, opening balance, deposit, withdrawal,
    and loan inputs.
-   [ ] Check that generated account numbers are unique.
-   [ ] Record interest calculations in transaction history.
-   [ ] Decide how loan disbursement and repayments should affect the
    account balance.
-   [ ] Include loan details in the generated statement.
-   [ ] Add JSON persistence so data survives after exit.
-   [ ] Add exception handling for invalid input and file errors.

## 🚀 Future Enhancements

Ideas for future versions:

-   💾 JSON-based permanent data storage.
-   🔐 Customer login and authentication.
-   🧾 Detailed statements with opening balance, credits, debits, and
    closing balance.
-   💳 Loan repayment and loan status management.
-   🔎 Search customers by name or account number.
-   📊 Transaction summaries and reports.
-   🧪 Unit tests for account creation, deposits, withdrawals, interest,
    and loans.
-   🧩 Split the project into separate modules for models, services,
    storage, and the main menu.

## 🎓 Learning Outcomes

This project provides practice with:

1.  Creating classes and methods using OOP.
2.  Storing structured data using lists and dictionaries.
3.  Searching and updating records with loops and conditions.
4.  Creating interactive menus using `match-case`.
5.  Generating IDs and timestamps with Python standard-library modules.
6.  Writing text files using file handling.
7.  Maintaining a transaction history for each account.
8.  Understanding how to identify and fix logical errors in a
    multi-feature application.

## ⚠️ Disclaimer

This project is created for educational and Python practice purposes
only. It is not connected to a real bank, payment gateway, or financial
institution. It does not implement secure authentication, encryption,
database transactions, audit controls, or regulatory compliance. Do not
enter real personal, banking, or financial information.

## 👨‍💻 Author

**Your Name**

-   GitHub: `<your-github-profile-link>`
-   Repository: `<your-repository-link>`

------------------------------------------------------------------------

```{=html}
<p align="center">
```
⭐ If this project helped you practice Python, consider giving the
repository a star!
```{=html}
</p>
```
