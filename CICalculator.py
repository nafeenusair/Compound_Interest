print("Compound Interest Calculator")

balance = 0
rate = 0
n = 0
t = 0

while balance <= 0:
    balance = float(input("Enter initial balance: "))
    if balance <= 0:
        print("Initial balance can't be less or equal to  0")

while rate <= 0:
    rate = float(input("Enter interest rate: "))
    rate = rate / 100
    if rate <= 0:
        print("Interest rate can't be less or equal to  0")

while n <= 0:
    n = int(input("Enter number of times interest is compounded per year: "))
    if n <= 0:
        print("Interest compounded per year can't be less or equal to  0")

while t <= 0:
    t = int(input("Enter total year(s): "))
    if t <= 0:
        print("year(s) can't be less or equal to  0")

final_amount = balance * pow((1 + rate / n), (n * t))
print(f"Your final amount is ${final_amount:,.2f}")