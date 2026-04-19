#Question16_A_OL
#Enter your name here: Arthur Drummond

print("Welcome to the Step Tracker App!")

name = input("Please enter your name: ")

steps_today = int(input("Enter the number of steps you walked today: ")) #this is where the user enters the number of steps

if steps_today < 0:
    print("The number of steps cannot be negative")
elif steps_today < 5000:
    print("Try to be more active today",name)

elif steps_today < 10000:
    print("Good effort",name,"Almost there.")
else:
    print("Well done",name,"you reached your goal!")
