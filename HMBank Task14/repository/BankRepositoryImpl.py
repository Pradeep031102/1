import pyodbc
from datetime import datetime
from repository.IBankRepository import IBankRepository

class BankRepositoryImpl(IBankRepository):
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-MB0Q7BK;DATABASE=HMBank;Trusted_Connection=True')
        self.cursor = self.conn.cursor()

    def create_account(self, acc_type, balance, customer_id):
        try:
            self.cursor.execute("INSERT INTO Accounts (account_type, balance, customer_id) VALUES (?, ?, ?)",(acc_type, balance, customer_id))
            self.conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error creating account: {e}")
            return False

    def list_accounts(self):
        try:
            self.cursor.execute("SELECT * FROM Accounts")
            accounts = self.cursor.fetchall()
            return accounts
        except pyodbc.Error as e:
            print(f"Error listing accounts: {e}")
            return []

    def calculate_interest(self):
        try:
            self.cursor.execute("SELECT * FROM Accounts WHERE account_type = 'Savings'")
            savings_accounts = self.cursor.fetchall()
            for acc in savings_accounts:
                interest_rate = 0.05  # Example interest rate
                interest = acc[3] * interest_rate
                new_balance = acc[3] + interest
                print(f"Interest Calculated : {interest}")
                print(f"New Balance : {new_balance}")
                self.cursor.execute("UPDATE Accounts SET balance = ? WHERE account_id = ?", (new_balance, acc[0]))
                self.conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error calculating interest: {e}")
            return False

    def get_account_balance(self, account_id):
        try:
            self.cursor.execute("SELECT balance FROM Accounts WHERE account_id = ?", (account_id,))
            balance = self.cursor.fetchone()
            if balance:
                return balance[0]
            else:
                return None
        except pyodbc.Error as e:
            print(f"Error getting account balance: {e}")
            return None

    def deposit(self, account_id, amount):
        try:
            current_balance = self.get_account_balance(account_id)
            if current_balance is not None:
                new_balance = current_balance + amount
                self.cursor.execute("UPDATE Accounts SET balance = ? WHERE account_id = ?", (new_balance, account_id))
                self.conn.commit()
                return new_balance
            else:
                return None
        except pyodbc.Error as e:
            print(f"Error depositing amount: {e}")
            return None

    def withdraw(self, account_id, amount):
        try:
            current_balance = self.get_account_balance(account_id)
            if current_balance is not None and current_balance >= amount:
                new_balance = current_balance - amount
                self.cursor.execute("UPDATE Accounts SET balance = ? WHERE account_id = ?", (new_balance, account_id))
                self.conn.commit()
                return new_balance
            else:
                return None
        except pyodbc.Error as e:
            print(f"Error withdrawing amount: {e}")
            return None

    def transfer(self, from_account_id, to_account_id, amount):
        try:
            from_balance = self.get_account_balance(from_account_id)
            to_balance = self.get_account_balance(to_account_id)
            if from_balance is not None and to_balance is not None and from_balance >= amount:
                new_from_balance = from_balance - amount
                new_to_balance = to_balance + amount
                self.cursor.execute("UPDATE Accounts SET balance = ? WHERE account_id = ?", (new_from_balance, from_account_id))
                self.cursor.execute("UPDATE Accounts SET balance = ? WHERE account_id = ?", (new_to_balance, to_account_id))
                self.conn.commit()
                return True
            else:
                return False
        except pyodbc.Error as e:
            print(f"Error transferring amount: {e}")
            return False

    def get_account_details(self, account_id):
        try:
            self.cursor.execute("SELECT * FROM Accounts WHERE account_id = ?", (account_id,))
            account_details = self.cursor.fetchone()
            if account_details:
                return account_details
            else:
                return None
        except pyodbc.Error as e:
            print(f"Error getting account details: {e}")
            return None

    def get_transactions(self, account_id, from_date, to_date):
        try:
            from_datetime = datetime.strptime(from_date, "%Y-%m-%d")
            to_datetime = datetime.strptime(to_date, "%Y-%m-%d")
            self.cursor.execute("SELECT * FROM Transactions WHERE account_id = ? AND transaction_date BETWEEN ? AND ?",
                                (account_id, from_datetime, to_datetime))
            transactions = self.cursor.fetchall()
            return transactions
        except pyodbc.Error as e:
            print(f"Error getting transactions: {e}")
            return []

    
    # Remember to close the connection when done
    def __del__(self):
        self.conn.close()
