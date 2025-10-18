#Author:Arthur drummond
#Date:17/10/2025
#A program that takes n numbers and prints the second largest of numbers inputted
numbers=[]
n = int(input("How many numbers do you want to input:"))

for i in range(1,n+1):
    no=float(input("Enter number:"))
    numbers.append(no)

max1= max(numbers)
numbers.remove(max1)

print("Of your",n,"numbers inputted the second largest is",max(numbers))
