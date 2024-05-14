from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_id):
        pass

    @abstractmethod
    def deposit(self, account_id, amount):
        pass

    @abstractmethod
    def withdraw(self, account_id, amount):
        pass

    @abstractmethod
    def transfer(self, from_account_id, to_account_id, amount):
        pass

    @abstractmethod
    def getAccountDetails(self, account_id):
        pass

    @abstractmethod
    def getTransactions(self, account_id, from_date, to_date):
        pass
