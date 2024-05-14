# Class and Objects

class Customer:
    def __init__(self, customer_id=0, first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}"

class Account:
    def __init__(self, account_number=0, account_type="", balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        interest_rate = 4.5
        interest_amount = (self.balance * interest_rate) / 100
        self.balance += interest_amount
        print(f"Interest calculated. New Balance: ${self.balance}")

class Bank:
    def main(self):
        customer = Customer(1, "John", "Doe", "john.doe@example.com", "123-456-7890", "123 Main St")
        account = Account(1001, "Savings", 1000.0)

        print("Customer Information:")
        print(customer)
        print("\nAccount Information:")
        print(f"Account Number: {account.account_number}\nAccount Type: {account.account_type}\nBalance: ${account.balance}")

        account.deposit(500)
        account.withdraw(200)
        account.calculate_interest()

if __name__ == "__main__":
    bank = Bank()
    bank.main()
