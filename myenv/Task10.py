# Has A Relation/ Association
import re

class Customer:
    def __init__(self, customer_id=0, first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}"

class Account:
    account_counter = 1000

    def __init__(self, account_type, customer, balance=0.0):
        self.account_number = Account.account_counter + 1
        self.account_type = account_type
        self.customer = customer
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def get_customer(self):
        return self.customer

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance."

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, customer, acc_type, balance):
        account = Account(acc_type, customer, balance)
        self.accounts.append(account)
        return account

    def get_account_balance(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account.get_balance()
        return "Account not found."

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account.deposit(amount)
        return "Account not found."

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account.withdraw(amount)
        return "Account not found."

    def transfer(self, from_account_number, to_account_number, amount):
        for account in self.accounts:
            if account.get_account_number() == from_account_number:
                withdraw_result = account.withdraw(amount)
                if isinstance(withdraw_result, float):
                    for acc in self.accounts:
                        if acc.get_account_number() == to_account_number:
                            acc.deposit(amount)
                            return withdraw_result
                else:
                    return withdraw_result
        return "Account not found."

    def getAccountDetails(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return "Account not found."

class BankApp:
    def __init__(self):
        self.bank = Bank()

    def main(self):
        while True:
            print("\nMenu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Details")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.transfer()
            elif choice == '5':
                self.get_account_details()
            elif choice == '6':
                print("Exiting Bank App.")
                break
            else:
                print("Invalid choice.")

    def create_account(self):
        print("\nAccount Types:")
        print("1. Savings")
        print("2. Current")
        acc_type_choice = input("Enter account type choice: ")

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email address: ")
        while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            email = input("Invalid email address. Please enter a valid email address: ")

        phone = input("Enter phone number: ")
        while not re.match(r"^\d{10}$", phone):
            phone = input("Invalid phone number. Please enter a 10-digit phone number: ")

        address = input("Enter address: ")
        balance = float(input("Enter initial balance: "))

        customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)
        account = self.bank.create_account(customer, "Savings" if acc_type_choice == '1' else "Current", balance)
        print(f"\nAccount created successfully!\nAccount Number: {account.get_account_number()}\nAccount Type: {account.get_account_type()}\nCustomer: {account.get_customer()}\nBalance: {account.get_balance()}")

    def deposit(self):
        account_number = int(input("Enter account number to deposit into: "))
        amount = float(input("Enter amount to deposit: "))
        balance = self.bank.deposit(account_number, amount)
        if isinstance(balance, float):
            print(f"Deposit successful. New Balance: ${balance}")
        else:
            print(balance)

    def withdraw(self):
        account_number = int(input("Enter account number to withdraw from: "))
        amount = float(input("Enter amount to withdraw: "))
        balance = self.bank.withdraw(account_number, amount)
        if isinstance(balance, float):
            print(f"Withdrawal successful. New Balance: ${balance}")
        else:
            print(balance)

    def transfer(self):
        from_account_number = int(input("Enter account number to transfer from: "))
        to_account_number = int(input("Enter account number to transfer to: "))
        amount = float(input("Enter amount to transfer: "))
        balance = self.bank.transfer(from_account_number, to_account_number, amount)
        if isinstance(balance, float):
            print(f"Transfer successful. New Balance in source account: ${balance}")
        else:
            print(balance)

    def get_account_details(self):
        account_number = int(input("Enter account number to get details: "))
        account_details = self.bank.getAccountDetails(account_number)
        if isinstance(account_details, str):
            print(account_details)
        else:
            print(f"\nAccount Number: {account_details.get_account_number()}\nAccount Type: {account_details.get_account_type()}\nCustomer: {account_details.get_customer()}\nBalance: {account_details.get_balance()}")

if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main()
