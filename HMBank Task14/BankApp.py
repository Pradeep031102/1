from datetime import datetime
from repository.BankRepositoryImpl import BankRepositoryImpl


class BankApp:
    def __init__(self):
        # Initialize necessary objects
        self.bank_service_provider = BankRepositoryImpl()

    def main_menu(self):
        # Implement main menu for banking operations
        while True:
            print("\nMain Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Account Details")
            print("6. List Accounts")
            print("7. Calculate Interest")
            print("8. Get Account Balance")
            print("9. Get Transactions")
            print("10. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account_menu()
            elif choice == "2":
                self.deposit_menu()
            elif choice == "3":
                self.withdraw_menu()
            elif choice == "4":
                self.transfer_menu()
            elif choice == "5":
                self.account_details_menu()
            elif choice == "6":
                self.list_accounts()
            elif choice == "7":
                self.calculate_interest()
            elif choice == "8":
                self.get_account_balance_menu()
            elif choice == "9":
                self.get_transactions_menu()
            elif choice == "10":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account_menu(self):
        # Implement submenu for creating different types of accounts
        print("\nCreate Account Menu:")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Zero Balance Account")
        choice = input("Enter account type to create: ")

        if choice == "1":
            self.create_savings_account()
        elif choice == "2":
            self.create_current_account()
        elif choice == "3":
            self.create_zero_balance_account()
        else:
            print("Invalid choice. Please try again.")

    def create_savings_account(self):
        # Implement logic to create a savings account
        customer_id = input("Enter customer ID: ")
        acc_no = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))
        if self.bank_service_provider.create_account('Savings', balance,customer_id):
            print("Savings account created successfully.")
        else:
            print("Error creating savings account.")

    def create_current_account(self):
        # Implement logic to create a current account
        customer_id = input("Enter customer ID: ")
        acc_no = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))
        if self.bank_service_provider.create_account('Current', balance, customer_id):
            print("Current account created successfully.")
        else:
            print("Error creating current account.")

    def create_zero_balance_account(self):
        # Implement logic to create a zero balance account
        customer_id = input("Enter customer ID: ")
        acc_no = input("Enter account number: ")
        if self.bank_service_provider.create_account('ZeroBalance', 0, customer_id):
            print("Zero balance account created successfully.")
        else:
            print("Error creating zero balance account.")

    def deposit_menu(self):
        # Implement deposit menu
        account_id = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        new_balance = self.bank_service_provider.deposit(account_id, amount)
        if new_balance is not None:
            print(f"Deposit successful. New balance: {new_balance}")
        else:
            print("Error depositing amount.")

    def withdraw_menu(self):
        # Implement withdraw menu
        account_id = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        new_balance = self.bank_service_provider.withdraw(account_id, amount)
        if new_balance is not None:
            print(f"Withdrawal successful. New balance: {new_balance}")
        else:
            print("Error withdrawing amount.")

    def transfer_menu(self):
        # Implement transfer menu
        from_account_id = input("Enter your account number: ")
        to_account_id = input("Enter recipient's account number: ")
        amount = float(input("Enter amount to transfer: "))
        if self.bank_service_provider.transfer(from_account_id, to_account_id, amount):
            print("Transfer successful.")
        else:
            print("Error transferring amount.")

    def account_details_menu(self):
        # Implement account details menu
        account_id = input("Enter account number: ")
        account_details = self.bank_service_provider.get_account_details(account_id)
        if account_details:
            print(f"Account Details:\n{account_details}")
        else:
            print("Account not found.")

    def list_accounts(self):
        # Implement list accounts functionality
        accounts_list = self.bank_service_provider.list_accounts()
        if accounts_list:
            print("List of Accounts:")
            for account in accounts_list:
                print(account)
        else:
            print("No accounts found.")

    def calculate_interest(self):
        # Implement calculate interest functionality
        if self.bank_service_provider.calculate_interest():
            print("Interest calculated successfully.")
        else:
            print("Error calculating interest.")

    def get_account_balance_menu(self):
        # Implement get account balance menu
        account_id = input("Enter account number: ")
        balance = self.bank_service_provider.get_account_balance(account_id)
        if balance is not None:
            print(f"Account Balance: {balance}")
        else:
            print("Error getting account balance.")

    def get_transactions_menu(self):
        # Implement get transactions menu
        account_id = input("Enter account number: ")
        from_date = input("Enter start date (YYYY-MM-DD): ")
        to_date = input("Enter end date (YYYY-MM-DD): ")
        transactions = self.bank_service_provider.get_transactions(account_id, from_date, to_date)
        if transactions:
            print("Transactions:")
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions found.")

    def run(self):
        # Start the banking application
        print("Welcome to the BankApp!")
        self.main_menu()


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.run()
