#author:Arthur Drummond
#04/09/25
#Description:Program that calculates and prints numbers in order of size

a=float(input("Enter a number:"))
b=float(input("Enter another number:"))
if (a<b):
    print(a,b)
elif (b<a):
    print(b,a)