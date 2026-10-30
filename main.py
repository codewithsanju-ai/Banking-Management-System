import uuid
import random
import datetime
import os


customer = []
customer_loan = []


# Custom exception
class AccountNotFoundError(Exception):
    pass


class BankManagement:

    # Common function: take integer input
    def get_integer(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    # Common function: find account
    def find_account(self, ac_num):
        for data in customer:
            if data["customer_accountnumber"] == ac_num:
                return data

        raise AccountNotFoundError("Account not found!")

    # 1. CREATE ACCOUNT
    def create_new(self):
        try:
            name = input("Enter your name: ").strip()

            if not name:
                raise ValueError("Name cannot be empty!")

            city = input("Enter your city: ").strip()

            if not city:
                raise ValueError("City cannot be empty!")

            number = input("Enter your 10 digit mobile number: ")

            if not number.isdigit() or len(number) != 10:
                raise ValueError("Mobile number must contain exactly 10 digits!")

            print("1. Current")
            print("2. Savings")

            choice = self.get_integer("Choose account type: ")

            match choice:
                case 1:
                    ac_type = "current"
                case 2:
                    ac_type = "savings"
                case _:
                    raise ValueError("Invalid account type!")

            opening_balance = self.get_integer("Enter opening balance: ")

            if opening_balance <= 0:
                raise ValueError("Opening balance must be greater than zero!")

            customer_id = str(uuid.uuid.uuid4()) if False else str(uuid.uuid4())
            ac_number = random.randint(100000000000, 999999999999)

            # Ensure account number is unique
            while any(
                data["customer_accountnumber"] == ac_number
                for data in customer
            ):
                ac_number = random.randint(100000000000, 999999999999)

            opening_date = datetime.datetime.now()

            customer.append({
                "customer_id": customer_id,
                "customer_accountnumber": ac_number,
                "customer_name": name,
                "customer_city": city,
                "customer_number": number,
                "account_type": ac_type,
                "opening_balance": opening_balance,
                "opening_date": opening_date,
                "transaction": []
            })

            print("\nAccount created successfully!")
            print("Account Number:", ac_number)
            print("Customer ID:", customer_id)

        except ValueError as e:
            print("Input Error:", e)

        except Exception as e:
            print("Unexpected Error:", e)

    # 2. DEPOSIT AMOUNT
    def deposit_am(self):
        try:
            ac_num = self.get_integer("Enter your account number: ")
            data = self.find_account(ac_num)

            deposit_am = self.get_integer("Enter deposit amount: ")

            if deposit_am <= 0:
                raise ValueError("Deposit amount must be greater than zero!")

            data["opening_balance"] += deposit_am

            data["transaction"].append({
                "type": "deposit",
                "amount": deposit_am,
                "date or time": datetime.datetime.now()
            })

            print("Amount deposited successfully!")
            print("Updated balance:", data["opening_balance"])

        except AccountNotFoundError as e:
            print(e)

        except ValueError as e:
            print("Input Error:", e)

    # 3. WITHDRAW AMOUNT
    def withdraw_am(self):
        try:
            ac_num = self.get_integer("Enter your account number: ")
            data = self.find_account(ac_num)

            withdraw_am = self.get_integer("Enter withdrawal amount: ")

            if withdraw_am <= 0:
                raise ValueError("Withdrawal amount must be greater than zero!")

            if withdraw_am > data["opening_balance"]:
                raise ValueError("Insufficient account balance!")

            data["opening_balance"] -= withdraw_am

            data["transaction"].append({
                "type": "withdraw",
                "amount": withdraw_am,
                "date or time": datetime.datetime.now()
            })

            print("Amount withdrawn successfully!")
            print("Updated balance:", data["opening_balance"])

        except AccountNotFoundError as e:
            print(e)

        except ValueError as e:
            print("Transaction Error:", e)

    # 4. CALCULATE INTEREST
    def calculate_interest(self):
        try:
            ac_num = self.get_integer("Enter your account number: ")
            data = self.find_account(ac_num)

            if data["account_type"] == "current":
                rate = 0.04
            else:
                rate = 0.07

            my_interest = data["opening_balance"] * rate

            data["opening_balance"] += my_interest

            data["transaction"].append({
                "type": "interest",
                "amount": my_interest,
                "date or time": datetime.datetime.now()
            })

            print("Interest rate:", rate * 100, "%")
            print("Interest amount:", my_interest)
            print("Updated balance:", data["opening_balance"])

        except AccountNotFoundError as e:
            print(e)

        except ValueError as e:
            print("Input Error:", e)

    # 5. TAKE LOAN
    def taking_loan(self):
        try:
            ac_num = self.get_integer("Enter your account number: ")
            data = self.find_account(ac_num)

            print("\nFill the required loan information")

            loan_am = self.get_integer("Enter loan amount: ")
            loan_int_rate = self.get_integer("Enter loan interest rate (%): ")
            loan_duration = self.get_integer("Enter loan duration (years): ")

            if loan_am <= 0:
                raise ValueError("Loan amount must be greater than zero!")

            if loan_int_rate < 0:
                raise ValueError("Interest rate cannot be negative!")

            if loan_duration <= 0:
                raise ValueError("Loan duration must be greater than zero!")

            loan_interest = (
                loan_am * loan_int_rate * loan_duration
            ) / 100

            payable_am = loan_am + loan_interest

            customer_loan.append({
                "customer-ac-number": data["customer_accountnumber"],
                "customer_name": data["customer_name"],
                "loan_amount": loan_am,
                "loan_interest_rate": loan_int_rate,
                "loan_duration": loan_duration,
                "loan_interest": loan_interest,
                "loan_total_payable": payable_am,
                "loan_status": "Active"
            })

            # Loan amount credited to customer account
            data["opening_balance"] += loan_am

            data["transaction"].append({
                "type": "loan credited",
                "amount": loan_am,
                "date or time": datetime.datetime.now()
            })

            print("\nLoan approved successfully!")
            print("Loan amount:", loan_am)
            print("Loan interest:", loan_interest)
            print("Total payable:", payable_am)
            print("Updated balance:", data["opening_balance"])

        except AccountNotFoundError as e:
            print(e)

        except ValueError as e:
            print("Loan Error:", e)

    # 6. GENERATE STATEMENT
    def generate_statement(self):
        try:
            ac_num = self.get_integer("Enter your account number: ")
            data = self.find_account(ac_num)

            filename = f"{ac_num}_summary.txt"

            with open(filename, "w", encoding="utf-8") as file:

                file.write("========== BANK ACCOUNT STATEMENT ==========\n\n")

                file.write(f"CUSTOMER ID       :: {data['customer_id']}\n")
                file.write(f"ACCOUNT NUMBER    :: {data['customer_accountnumber']}\n")
                file.write(f"CUSTOMER NAME     :: {data['customer_name']}\n")
                file.write(f"CUSTOMER CITY     :: {data['customer_city']}\n")
                file.write(f"MOBILE NUMBER     :: {data['customer_number']}\n")
                file.write(f"ACCOUNT TYPE      :: {data['account_type']}\n")
                file.write(f"OPENING BALANCE   :: {data['opening_balance']}\n")
                file.write(f"OPENING DATE      :: {data['opening_date']}\n")

                file.write("\n========== TRANSACTION HISTORY ==========\n")

                if not data["transaction"]:
                    file.write("No transactions found.\n")

                for tran in data["transaction"]:
                    file.write("------------------------------------------\n")
                    file.write(f"TYPE       :: {tran['type']}\n")
                    file.write(f"AMOUNT     :: {tran['amount']}\n")
                    file.write(f"DATE/TIME  :: {tran['date or time']}\n")

                file.write("\n========== LOAN DETAILS ==========\n")

                loans = [
                    loan for loan in customer_loan
                    if loan["customer-ac-number"] == ac_num
                ]

                if not loans:
                    file.write("No loan records found.\n")

                for loan in loans:
                    file.write("------------------------------------------\n")
                    file.write(f"LOAN AMOUNT    :: {loan['loan_amount']}\n")
                    file.write(f"INTEREST RATE  :: {loan['loan_interest_rate']}%\n")
                    file.write(f"DURATION       :: {loan['loan_duration']} years\n")
                    file.write(f"INTEREST       :: {loan['loan_interest']}\n")
                    file.write(f"TOTAL PAYABLE  :: {loan['loan_total_payable']}\n")
                    file.write(f"STATUS         :: {loan['loan_status']}\n")

            print("Statement generated successfully!")
            print("File name:", filename)

        except AccountNotFoundError as e:
            print(e)

        except PermissionError:
            print("Permission denied! Close the statement file if it is already open.")

        except OSError as e:
            print("File handling error:", e)

        except ValueError as e:
            print("Input Error:", e)

        finally:
            print("Statement operation completed.")

    # 7. DISPLAY SINGLE CUSTOMER
    def display_SingleAccount(self):
        try:
            ac_num = self.get_integer("Enter your account number: ")
            data = self.find_account(ac_num)

            print("\n========== CUSTOMER DETAILS ==========")
            print("CUSTOMER ID      :", data["customer_id"])
            print("CUSTOMER NAME    :", data["customer_name"])
            print("ACCOUNT NUMBER   :", data["customer_accountnumber"])
            print("CITY             :", data["customer_city"])
            print("MOBILE NUMBER    :", data["customer_number"])
            print("ACCOUNT TYPE     :", data["account_type"])
            print("ACCOUNT BALANCE  :", data["opening_balance"])

            total_credit = sum(
                t["amount"] for t in data["transaction"]
                if t["type"] in ["deposit", "interest", "loan credited"]
            )

            total_debit = sum(
                t["amount"] for t in data["transaction"]
                if t["type"] == "withdraw"
            )

            print("TOTAL CREDIT     :", total_credit)
            print("TOTAL DEBIT      :", total_debit)

            loans = [
                loan for loan in customer_loan
                if loan["customer-ac-number"] == ac_num
            ]

            total_loan = sum(loan["loan_amount"] for loan in loans)

            print("TOTAL LOAN       :", total_loan)

        except AccountNotFoundError as e:
            print(e)

        except ValueError as e:
            print("Input Error:", e)

    # 8. DISPLAY ALL CUSTOMERS
    def display_customer(self):

        try:
            if not customer:
                raise LookupError("No customer records found!")

            print("\n========== ALL CUSTOMER DETAILS ==========")

            for data in customer:
                print("------------------------------------------")
                print("CUSTOMER ID     :", data["customer_id"])
                print("CUSTOMER NAME   :", data["customer_name"])
                print("ACCOUNT NUMBER  :", data["customer_accountnumber"])
                print("ACCOUNT TYPE    :", data["account_type"])
                print("ACCOUNT BALANCE :", data["opening_balance"])

            print("------------------------------------------")
            print("TOTAL CUSTOMERS:", len(customer))

        except LookupError as e:
            print(e)

    # 9. CLOSE ACCOUNT
    def close_ac(self):
        try:
            ac_num = self.get_integer("Enter your account number: ")
            data = self.find_account(ac_num)

            print("Do you really want to close your account?")
            print("1. Yes")
            print("2. No")

            choice = self.get_integer("Enter your choice: ")

            match choice:
                case 1:
                    customer.remove(data)

                    # Remove associated loan records too
                    customer_loan[:] = [
                        loan for loan in customer_loan
                        if loan["customer-ac-number"] != ac_num
                    ]

                    print("Account closed successfully!")

                case 2:
                    print("Account closing cancelled.")

                case _:
                    raise ValueError("Invalid choice!")

        except AccountNotFoundError as e:
            print(e)

        except ValueError as e:
            print("Input Error:", e)


# MAIN PROGRAM

b1 = BankManagement()

try:
    while True:

        print("\n========== WELCOME TO BANKING MANAGEMENT SYSTEM ==========")
        print("1. Create an account")
        print("2. Deposit amount")
        print("3. Withdraw amount")
        print("4. Check interest")
        print("5. Take loan")
        print("6. Generate statement")
        print("7. Display single customer")
        print("8. Display all customers")
        print("9. Close account")
        print("10. Exit")

        try:
            choice1 = int(input("Enter your choice: "))

            match choice1:
                case 1:
                    b1.create_new()

                case 2:
                    b1.deposit_am()

                case 3:
                    b1.withdraw_am()

                case 4:
                    b1.calculate_interest()

                case 5:
                    b1.taking_loan()

                case 6:
                    b1.generate_statement()

                case 7:
                    b1.display_SingleAccount()

                case 8:
                    b1.display_customer()

                case 9:
                    b1.close_ac()

                case 10:
                    print("Thanks for using our banking system!")
                    break

                case _:
                    raise ValueError("Please select a valid menu option!")

        except ValueError as e:
            print("Menu Error:", e)

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")

finally:
    print("Banking system closed.")