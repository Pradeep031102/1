from datetime import datetime

class Transaction:
    def __init__(self, account, description, transaction_type, amount):
        self.account = account
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount
        self.date_time = datetime.now()
