# Abstraction

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number=0, customer_name="", balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def get_customer_name(self):
        return self.customer_name

    def get_balance(self):
        return self.balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, account_number=0, customer_name="", balance=0.0, interest_rate=4.5):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

    def calculate_interest(self):
        interest_amount = (self.balance * self.interest_rate) / 100
        self.balance += interest_amount
        print(f"Interest calculated. New Balance: ${self.balance}")

class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 1000  # Example overdraft limit

    def __init__(self, account_number=0, customer_name="", balance=0.0):
        super().__init__(account_number, customer_name, balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance + self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Withdrawal amount exceeds available balance and overdraft limit.")

    def calculate_interest(self):
        print("Current accounts do not earn interest.")

class Bank:
    def main(self):
        while True:
            print("1. Create Savings Account")
            print("2. Create Current Account")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_savings_account()
            elif choice == '2':
                self.create_current_account()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")

    def create_savings_account(self):
        account_number = int(input("Enter account number: "))
        customer_name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))
        interest_rate = float(input("Enter interest rate (%): "))
        savings_account = SavingsAccount(account_number, customer_name, initial_balance, interest_rate)
        self.operate_account(savings_account)

    def create_current_account(self):
        account_number = int(input("Enter account number: "))
        customer_name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))
        current_account = CurrentAccount(account_number, customer_name, initial_balance)
        self.operate_account(current_account)

    def operate_account(self, account):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '3':
                account.calculate_interest()
            elif choice == '4':
                print("Exiting account operations.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    bank = Bank()
    bank.main()
