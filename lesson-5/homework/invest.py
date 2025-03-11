amount = float(input("Enter the initial amount: "))
rate = float(input("Enter the annual rate: "))
years = int(input("Enter the number of years: "))

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount *= (1 + 0.01 * rate)
        print(f"Year {year}: ${amount:.2f}")
invest(amount, rate, years)
