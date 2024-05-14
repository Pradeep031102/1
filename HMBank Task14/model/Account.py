class Account:
    last_acc_no = 1000
    def __init__(self, account_type, balance, customer):
        self.account_id = Account.last_acc_no + 1
        self.account_type = account_type
        self.balance = balance
        self.customer = customer
        Account.last_acc_no += 1
