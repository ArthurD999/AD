#author:Arthur Drummond
#06/09/25
#Description:Program that accepts number and gives response on size of number
num=float(input("Enter a number:"))
if num < 10:
    print("Too low")
elif num > 10 and num <20:
    print("Correct")
else:
    print("Too high")