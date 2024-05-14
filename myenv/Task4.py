# Looping, Array and Data Validation

def check_account_balance(accounts, account_number):
    for account in accounts:
        if account['account_number'] == account_number:
            print(f"Account Balance: {account['balance']}")
            return
    print("Invalid account number.")

# Assuming accounts is a list of dictionaries with account_number and balance
accounts = [{'account_number': '123456', 'balance': 5000}, {'account_number': '789012', 'balance': 10000}]

while True:
    account_number = input("Enter your account number: ")
    check_account_balance(accounts, account_number)
    choice = input("Do you want to check another account? (yes/no): ")
    if choice.lower() != 'yes':
        break
