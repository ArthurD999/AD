#author:Arthur Drummond
#02/09/25
#Description:Program inputs slices of pizza and eatedn and gives how many left

slicesStartedWith = input("How many pizza slices did you start with?:")
slicesStartedWith = int(slicesStartedWith)
eaten = input("How many have you eaten")
eaten = int(eaten)
print("You have",slicesStartedWith-eaten,"slices left")