#Author:Arthur drummond
#Date:10/7/2025
#A program that checks calculates whether inputted number are even or odd
even=0
odd=0
sigma=67
while sigma ==67:
    num=int(input("Enter numbers and when your finished enter 0: "))
    if num%2==0 and num!=0:
        even+=1
    elif num%2!=0:
        odd+=1
    else:
        sigma=66
    
print("There is",even,"even number and",odd,"odd numbers")


