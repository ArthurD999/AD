#Author:Arthur drummond
#Date:17/10/2025

n=int(input("Enter a number:"))
m=int(input("Enter your divisor:"))

for i in range(1,n+1):
    if i % m ==0:
        print(i)
        if i % 2 ==0:
            print("Even")
        else:
            print("Odd")
