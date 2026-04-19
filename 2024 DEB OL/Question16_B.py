# Question 16(b)
# Name and School: Arthur

principal = float(input("Enter the principal investment amount: €"))
rate = float(input("Enter the annual interest rate (e.g. 0.05 for 5% interest): "))

value = principal

for year in range(1, 11):
    value = round(value * (1 + rate), 2)
    print("Year", year, "- Investment value: €" + str(value))
