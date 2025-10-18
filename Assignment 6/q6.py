num=0
total=0
user_input=0
while num<=user_input:
    user_input=float(input("Enter an number:"))
    total+=user_input
    if total>50:
        break
    
print(total)
         