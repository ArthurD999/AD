#Author:Arthur drummond
#Date:14/10/2025
#A program that
n=int(input("Enter a number more than 20:"))
for i in range(11,n):
    print(i)
    if i%3==0 and i%7==0:
        print("TipsyTopsy")
    elif i%3==0:
        print("Tipsy")
    elif i%7==0:
        print("Topsy")