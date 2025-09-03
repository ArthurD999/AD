#author:Arthur Drummond
#02/09/25
#Description:Program that calculates simple and compound interest
sOrc=input("Type 1 to calculate simple interest and 2 for compound:")
if "1" in sOrc:
    principal=float(input("Enter the principal:"))
    rate=float(input("Enter the rate of interest:"))
    time=float(input("Enter the amount of time in years:"))
    print(principal*rate*time/100)
else:
    principal1=float(input("Enter the principal:"))
    rate1=float(input("Enter the rate of interest:"))
    time1=float(input("Enter the amount of time in years:"))
    print(principal1*(1+rate1/100)**time1)





