#Author:Arthur drummond
#Date:10/7/2025
#A program that checks whether a number is an armstrong number
count=0
power=0
num=(input("Enter a number:"))

for i in num:
    power=power+1

for i in num:
    i=int(i)
    count+=i**power

num=int(num)    

if count==num:
    print("This is an armstrong number",count)
else:
    print("This is not an armstrong number",count)

    