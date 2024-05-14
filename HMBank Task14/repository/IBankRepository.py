from abc import ABC, abstractmethod

class IBankRepository(ABC):
    @abstractmethod
    def create_account(self, customer, acc_no, acc_type, balance):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

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
    def get_account_details(self, account_id):
        pass

    @abstractmethod
    def get_transactions(self, account_id, from_date, to_date):
        pass
