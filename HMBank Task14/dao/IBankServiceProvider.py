from abc import ABC, abstractmethod

class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, acc_no, acc_type, balance):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def getAccountDetails(self, account_id):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass
