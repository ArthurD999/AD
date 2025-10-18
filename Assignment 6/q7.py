correct =0
while correct != 1:
    num=int(input("Enter a number"))
    if num>20:
        print("Too high")
    elif num<10:
        print("Too low")
    elif num>10 and num<20:
        correct=1
    
    
print("Thank you")
