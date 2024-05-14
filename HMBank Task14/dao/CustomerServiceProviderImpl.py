from dao.ICustomerServiceProvider import ICustomerServiceProvider

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}  # Dictionary to store account balances

    def get_account_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            return 0.0  # Account not found, return 0 balance

    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id] += amount
            return self.accounts[account_id]  # Return updated balance
        else:
            return 0.0  # Account not found, deposit failed

    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            if self.accounts[account_id] >= amount:
                self.accounts[account_id] -= amount
                return self.accounts[account_id]  # Return updated balance
            else:
                return 0.0  # Insufficient balance, withdraw failed
        else:
            return 0.0  # Account not found, withdraw failed

    def transfer(self, from_account_id, to_account_id, amount):
        if from_account_id in self.accounts and to_account_id in self.accounts:
            if self.accounts[from_account_id] >= amount:
                self.accounts[from_account_id] -= amount
                self.accounts[to_account_id] += amount
                return True  # Transfer successful
            else:
                return False  # Insufficient balance, transfer failed
        else:
            return False  # Account not found, transfer failed

    def get_account_details(self, account_id):
        # Placeholder implementation without database interaction
        if account_id in self.accounts:
            return f"Account Number: {account_id}, Balance: {self.accounts[account_id]}"
        else:
            return None  # Account not found

    def get_transactions(self, account_id, from_date, to_date):
        # Placeholder implementation without database interaction
        return []  # Placeholder empty list for transactions
