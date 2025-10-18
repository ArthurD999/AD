#author:Arthur Drummond
#02/09/25
#Description:Program that calculates simple and compound interest
sOrc=input("Type 1 to calculate simple interest and 2 for compound:")
if sOrc == 1:
    principal=float(input("Enter the principal:"))
    rate=float(input("Enter the rate of interest:"))
    time=float(input("Enter the amount of time in years:"))
    print(principal*rate*time/100+principal)
elif sOrc == 2:
    principal=float(input("Enter the principal:"))
    rate=float(input("Enter the rate of interest:"))
    time=float(input("Enter the amount of time in years:"))
    print(principal*(1+rate/100)**time)





