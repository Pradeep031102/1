from model.Account import Account

class CurrentAccount(Account):
    def __init__(self, account_type, balance, customer, overdraft_limit):
        super().__init__(account_type, balance, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return True
        else:
            return False
