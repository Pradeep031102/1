# Inheritance and Polymorphism

class Account:
    def __init__(self, account_number=0, account_type="", balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        pass  # Default implementation, overridden in subclasses

class SavingsAccount(Account):
    def __init__(self, account_number=0, balance=0.0, interest_rate=4.5):
        super().__init__(account_number, "Savings", balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = (self.balance * self.interest_rate) / 100
        self.balance += interest_amount
        print(f"Interest calculated. New Balance: ${self.balance}")

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000  # Example overdraft limit

    def __init__(self, account_number=0, balance=0.0, overdraft_limit=1000):
        super().__init__(account_number, "Current", balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

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
        initial_balance = float(input("Enter initial balance: "))
        interest_rate = float(input("Enter interest rate (%): "))
        savings_account = SavingsAccount(account_number, initial_balance, interest_rate)
        self.operate_account(savings_account)

    def create_current_account(self):
        account_number = int(input("Enter account number: "))
        initial_balance = float(input("Enter initial balance: "))
        overdraft_limit = float(input("Enter overdraft limit: "))
        current_account = CurrentAccount(account_number, initial_balance, overdraft_limit)
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
