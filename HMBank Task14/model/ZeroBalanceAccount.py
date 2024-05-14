from model.Account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, account_type, customer):
        super().__init__(account_type, 0, customer)
