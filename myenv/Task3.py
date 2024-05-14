# Lopping Structures

def calculate_future_balance(initial_balance, annual_interest_rate, years):
    for year in range(1, years + 1):
        future_balance = initial_balance * (1 + annual_interest_rate/100) ** year
        print(f"Year {year}: Future balance is {future_balance:.2f}")

initial_balance = float(input("Enter initial balance: "))
annual_interest_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

calculate_future_balance(initial_balance, annual_interest_rate, years)
