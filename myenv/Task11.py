#  Interface/abstract class, and Single Inheritance, static variable
from abc import ABC, abstractmethod

# Customer class
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

# ICustomerServiceProvider interface
class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_number):
        pass

    @abstractmethod
    def deposit(self, account_number, amount):
        pass

    @abstractmethod
    def withdraw(self, account_number, amount):
        pass

    @abstractmethod
    def transfer(self, from_account_number, to_account_number, amount):
        pass

    @abstractmethod
    def getAccountDetails(self, account_number):
        pass

# IBankServiceProvider interface
class IBankServiceProvider(ICustomerServiceProvider, ABC):
    @abstractmethod
    def create_account(self, customer, accNo, accType, balance):
        pass

    @abstractmethod
    def listAccounts(self):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass

# Account class
class Account:
    lastAccNo = 1000  # Static variable

    def __init__(self, account_type, customer, balance=0.0):
        Account.lastAccNo += 1
        self.account_number = Account.lastAccNo
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

# SavingsAccount class inheriting from Account
class SavingsAccount(Account):
    def __init__(self, customer, balance=500, interest_rate=4.5):
        super().__init__("Savings", customer, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = (self.balance * self.interest_rate) / 100
        self.balance += interest_amount
        return interest_amount

# CurrentAccount class inheriting from Account
class CurrentAccount(Account):
    def __init__(self, customer, balance=0.0, overdraft_limit=1000):
        super().__init__("Current", customer, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        else:
            return False

# ZeroBalanceAccount class inheriting from Account
class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("Zero Balance", customer)

# CustomerServiceProviderImpl implementing ICustomerServiceProvider
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accountList = []

    def get_account_balance(self, account_number):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                return account.get_balance()
        return "Account not found."

    def deposit(self, account_number, amount):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                account.deposit(amount)
                return account.get_balance()
        return "Account not found."

    def withdraw(self, account_number, amount):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                if isinstance(account, SavingsAccount) and account.get_balance() - amount < 500:
                    return "Withdrawal violates minimum balance rule."
                elif account.withdraw(amount):
                    return account.get_balance()
                else:
                    return "Insufficient funds."
        return "Account not found."

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = None
        to_account = None
        for account in self.accountList:
            if account.get_account_number() == from_account_number:
                from_account = account
            elif account.get_account_number() == to_account_number:
                to_account = account
        if from_account and to_account:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                return from_account.get_balance()
            else:
                return "Insufficient funds."
        else:
            return "Account not found."

    def getAccountDetails(self, account_number):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                return account
        return "Account not found."

# BankServiceProviderImpl inheriting from CustomerServiceProviderImpl and implementing IBankServiceProvider
class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def create_account(self, customer, accNo, accType, balance):
        if accType == "Savings":
            account = SavingsAccount(customer, balance)
        elif accType == "Current":
            account = CurrentAccount(customer, balance)
        else:
            account = ZeroBalanceAccount(customer)
        self.accountList.append(account)
        return account

    def listAccounts(self):
        return self.accountList

    def calculateInterest(self):
        for account in self.accountList:
            if isinstance(account, SavingsAccount):
                account.calculate_interest()

# BankApp class
class BankApp:
    def __init__(self):
        self.bankServiceProvider = BankServiceProviderImpl()

    def main(self):
        while True:
            print("\nMenu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Balance")
            print("6. Get Account Details")
            print("7. Exit")
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
                self.get_account_balance()
            elif choice == '6':
                self.get_account_details()
            elif choice == '7':
                print("Exiting Bank App.")
                break
            else:
                print("Invalid choice.")

    def create_account(self):
        print("\nAccount Types:")
        print("1. Savings")
        print("2. Current")
        print("3. Zero Balance")
        acc_type = input("Enter account type: ")
        customer_id = int(input("Enter customer ID: "))  # Assume you have customer ID
        customer = Customer(customer_id)  # Create customer object based on ID
        balance = float(input("Enter initial balance: "))
        self.bankServiceProvider.create_account(customer, acc_type, balance)
        print("Account created successfully.")

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))
        balance = self.bankServiceProvider.deposit(account_number, amount)
        if isinstance(balance, str):
            print(balance)
        else:
            print(f"Deposit successful. Current balance: {balance}")

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))
        balance = self.bankServiceProvider.withdraw(account_number, amount)
        if isinstance(balance, str):
            print(balance)
        else:
            print(f"Withdrawal successful. Current balance: {balance}")

    def transfer(self):
        from_account_number = int(input("Enter account number to transfer from: "))
        to_account_number = int(input("Enter account number to transfer to: "))
        amount = float(input("Enter amount to transfer: "))
        balance = self.bankServiceProvider.transfer(from_account_number, to_account_number, amount)
        if isinstance(balance, str):
            print(balance)
        else:
            print(f"Transfer successful. Current balance: {balance}")

    def get_account_balance(self):
        account_number = int(input("Enter account number: "))
        balance = self.bankServiceProvider.get_account_balance(account_number)
        if isinstance(balance, str):
            print(balance)
        else:
            print(f"Account balance: {balance}")

    def get_account_details(self):
        account_number = int(input("Enter account number: "))
        details = self.bankServiceProvider.getAccountDetails(account_number)
        if isinstance(details, str):
            print(details)
        else:
            print(details)

# Main function to run the BankApp
if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main()
