from model.Account import Account

class SavingsAccount(Account):
    def __init__(self, account_type, balance, customer, interest_rate):
        super().__init__(account_type, balance, customer)
        self.interest_rate = interest_rate
        self.minimum_balance = 500

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)
