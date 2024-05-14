# Bank Transaction History

transactions = []

while True:
    transaction_type = input("Enter transaction type (Deposit/Withdraw/Exit): ")
    if transaction_type.lower() == 'exit':
        break
    amount = float(input("Enter amount: "))
    transactions.append((transaction_type, amount))

print("Transaction History:")
for idx, transaction in enumerate(transactions, 1):
    print(f"{idx}. {transaction[0]}: {transaction[1]}")
