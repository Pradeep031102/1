from abc import ABC, abstractmethod
from collections import defaultdict
from random import randint

# Custom Exceptions
class InsufficientFundException(Exception):
    def __init__(self, message="Insufficient funds in the account."):
        self.message = message
        super().__init__(self.message)

class InvalidAccountException(Exception):
    def __init__(self, message="Invalid account number."):
        self.message = message
        super().__init__(self.message)

class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Overdraft limit exceeded for current account."):
        self.message = message
        super().__init__(self.message)

# Customer class
class Customer:
    def __init__(self, customer_id, first_name='', last_name='', email='', phone='', address=''):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

# Account abstract class
class Account(ABC):
    def __init__(self, customer, account_number, balance=0):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

# SavingsAccount class
class SavingsAccount(Account):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer, account_number, balance)
        self.interest_rate = 4.5  # Fixed interest rate for savings account

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 500:
            self.balance -= amount
            return True
        else:
            raise InsufficientFundException()

    def calculate_interest(self):
        self.balance += (self.balance * self.interest_rate / 100)

# CurrentAccount class
class CurrentAccount(Account):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer, account_number, balance)
        self.overdraft_limit = 10000  # Overdraft limit for current account

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        else:
            raise OverDraftLimitExceededException()

    def calculate_interest(self):
        pass  # Current account does not have interest

# ZeroBalanceAccount class
class ZeroBalanceAccount(Account):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer, account_number, balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            raise InsufficientFundException()

    def calculate_interest(self):
        pass  # Zero balance account does not have interest

# Interfaces/Abstract Classes
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

class IBankServiceProvider(ICustomerServiceProvider):
    @abstractmethod
    def create_account(self, customer, accType, balance):
        pass

    @abstractmethod
    def listAccounts(self):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass

# BankServiceProviderImpl class using List of Accounts
class BankServiceProviderImpl(IBankServiceProvider,ICustomerServiceProvider):
    def __init__(self):
        super().__init__()
        self.accountList = []  # List of Accounts

    def generate_account_number(self):
        return randint(1001, 9999)

    def create_account(self, customer, accType, balance):
        account_number = self.generate_account_number()
        if accType == "Savings":
            account = SavingsAccount(customer, account_number, balance)
        elif accType == "Current":
            account = CurrentAccount(customer, account_number, balance)
        else:
            account = ZeroBalanceAccount(customer, account_number)
        self.accountList.append(account)
        return account

    def get_account_balance(self, account_number):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                return account.get_balance()
        raise InvalidAccountException()

    def deposit(self, account_number, amount):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                account.deposit(amount)
                return account.get_balance()
        raise InvalidAccountException()

    def withdraw(self, account_number, amount):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                if account.withdraw(amount):
                    return account.get_balance()
                else:
                    raise InsufficientFundException()
        raise InvalidAccountException()

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
                return True
            else:
                raise InsufficientFundException()
        else:
            raise InvalidAccountException()

    def getAccountDetails(self, account_number):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                return account
        raise InvalidAccountException()

    def listAccounts(self):
        sorted_accounts = sorted(self.accountList, key=lambda x: (x.customer.first_name, x.customer.last_name))
        return sorted_accounts

    def calculateInterest(self):
        for account in self.accountList:
            if isinstance(account, SavingsAccount):
                account.calculate_interest()

# BankApp class
class BankApp:
    def __init__(self):
        self.bank_service = BankServiceProviderImpl()

    def display_menu(self):
        print("Banking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Get Account Balance")
        print("6. Get Account Details")
        print("7. List Accounts")
        print("8. Calculate Interest")
        print("9. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    self.create_account_menu()
                elif choice == "2":
                    self.deposit_menu()
                elif choice == "3":
                    self.withdraw_menu()
                elif choice == "4":
                    self.transfer_menu()
                elif choice == "5":
                    self.get_account_balance_menu()
                elif choice == "6":
                    self.get_account_details_menu()
                elif choice == "7":
                    self.list_accounts_menu()
                elif choice == "8":
                    self.calculate_interest_menu()
                elif choice == "9":
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except (InsufficientFundException, InvalidAccountException, OverDraftLimitExceededException) as e:
                print(e)

    def create_account_menu(self):
        print("Creating Account...")
        customer_id = int(input("Enter Customer ID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email Address: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        acc_type = input("Enter Account Type (Savings/Current/ZeroBalance): ")
        balance = float(input("Enter Initial Balance: "))
        customer = Customer(customer_id, first_name, last_name, email, phone, address)
        self.bank_service.create_account(customer, acc_type, balance)
        print("Account created successfully.")

    def deposit_menu(self):
        print("Deposit to Account...")
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))
        balance = self.bank_service.deposit(account_number, amount)
        print(f"Deposit successful. Updated Balance: {balance}")

    def withdraw_menu(self):
        print("Withdraw from Account...")
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdrawal Amount: "))
        balance = self.bank_service.withdraw(account_number, amount)
        print(f"Withdrawal successful. Updated Balance: {balance}")

    def transfer_menu(self):
        print("Transfer between Accounts...")
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Transfer Amount: "))
        self.bank_service.transfer(from_account_number, to_account_number, amount)
        print("Transfer successful.")

    def get_account_balance_menu(self):
        print("Get Account Balance...")
        account_number = int(input("Enter Account Number: "))
        balance = self.bank_service.get_account_balance(account_number)
        print(f"Account Balance: {balance}")

    def get_account_details_menu(self):
        print("Get Account Details...")
        account_number = int(input("Enter Account Number: "))
        account = self.bank_service.getAccountDetails(account_number)
        print(f"Account Details:\n{account.__dict__}")

    def list_accounts_menu(self):
        print("List of Accounts:")
        accounts = self.bank_service.listAccounts()
        for account in accounts:
            print(f"Account Number: {account.account_number}, Customer Name: {account.customer.first_name} {account.customer.last_name}, Balance: {account.balance}")

    def calculate_interest_menu(self):
        print("Calculating Interest...")
        self.bank_service.calculateInterest()
        print("Interest calculated and added to savings accounts.")

# Main function
if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.run()
