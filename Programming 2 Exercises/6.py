#author:Arthur Drummond
#06/09/25
#Description:Program that asks user age and responds based on age
userAge=int(input("What is your age:"))
if userAge>18:
    print("You can vote")
elif userAge == 17:
    print("You can learn to drive")
elif userAge ==16:
    print("You can buy a lottery ticket")
elif userAge <16:
    print("You can go trick or treating")
    