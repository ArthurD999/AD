
count=0
correct =66
while correct != 67:
    num=int(input("Enter a number"))
    if num>67:
        print("Too high")
    elif num<67:
        print("Too low")
    elif num==67:
        correct=67
    count+=1
    
    
print("Thank you it took",count,"attempts")