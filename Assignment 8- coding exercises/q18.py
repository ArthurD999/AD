#Author:Arthur drummond
#Date:17/10/2025
digits=0
significant=0
x=input("Enter an integer:")

for i in x:
   digits+=1


for i in x:
   if i != 0:
        significant = i
   break    

y=int(significant+str(digits))

print(y)
