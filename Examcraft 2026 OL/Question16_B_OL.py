#Question16_B_OL
#Enter your name here: Arthur Drummond

print("Welcome to my weekly step tracker!")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = []

for day in days:
    step_count = int(input("Please enter the steps you did on " + day + ": "))
    
    steps.append(step_count)

print("The list of steps is:", steps)

print("The total steps taken this week was:", sum(steps))
print("The average number of steps is:", round(sum(steps) / len(steps), 2))

print("The largest number of steps you took this week was:", max(steps))
print("The smallest number of steps you took this week was:", min(steps))
