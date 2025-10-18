#Author:Arthur drummond
#Date:10/7/2025
#A program that converts binary to decimal

count=0
power=-1
num=input("Enter a binary number:")

for i in num:
 i=int(i)
 if i ==1:
    count+=i*2**power
 power-=1
     
print(count)
    