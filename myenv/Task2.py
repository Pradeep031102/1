# Nested Conditional Statements

def atm_transaction(balance, transaction_type, amount):
    if transaction_type == "Check Balance":
        print(f"Your current balance is {balance}.")
    elif transaction_type == "Withdraw":
        if amount > balance:
            print("Insufficient balance.")
        elif amount % 100 != 0 or amount % 500 != 0:
            print("Withdrawal amount must be in multiples of 100 or 500.")
        else:
            balance -= amount
            print(f"Withdrawal successful. Your new balance is {balance}.")
    elif transaction_type == "Deposit":
        balance += amount
        print(f"Deposit successful. Your new balance is {balance}.")

balance = float(input("Enter your current balance: "))
transaction_type = input("Enter transaction type (Check Balance/Withdraw/Deposit): ")
amount = float(input("Enter amount: "))

atm_transaction(balance, transaction_type, amount)
