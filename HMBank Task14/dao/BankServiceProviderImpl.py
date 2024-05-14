from dao.IBankServiceProvider import IBankServiceProvider
class BankServiceProviderImpl(IBankServiceProvider):
    def __init__(self):
        super().__init__()
        self.account_details = {}  # Dictionary to store account details

    def create_account(self, customer, acc_no, acc_type, balance):
        # Placeholder implementation without database interaction
        if acc_no not in self.accounts:
            if acc_type == 'Savings':
                if balance >= 500:  # Minimum balance for savings account
                    self.accounts[acc_no] = balance
                    self.account_details[acc_no] = {'Customer': customer, 'Type': acc_type, 'Balance': balance}
                    return True  # Account created successfully
                else:
                    return False  # Insufficient balance for savings account
            elif acc_type == 'Current':
                self.accounts[acc_no] = balance
                self.account_details[acc_no] = {'Customer': customer, 'Type': acc_type, 'Balance': balance}
                return True  # Account created successfully
            elif acc_type == 'ZeroBalance':
                self.accounts[acc_no] = 0  # Zero balance for zero balance account
                self.account_details[acc_no] = {'Customer': customer, 'Type': acc_type, 'Balance': 0}
                return True  # Account created successfully
        else:
            return False  # Account already exists

    def list_accounts(self):
        # Placeholder implementation without database interaction
        return self.account_details.values()  # Return list of account details

    def calculate_interest(self):
        # Placeholder implementation without database interaction
        for acc_no, details in self.account_details.items():
            if details['Type'] == 'Savings':
                interest_rate = 0.05  # Example interest rate for savings account
                interest = details['Balance'] * interest_rate
                self.accounts[acc_no] += interest  # Add interest to balance

    def getAccountDetails(self, account_id):
        # Placeholder implementation without database interaction
        if account_id in self.account_details:
            return self.account_details[account_id]
        else:
            return None  # Account not found
