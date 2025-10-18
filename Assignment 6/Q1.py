#Arthur Drummond
#2/10/25
#A program that averages inputed numbers
user_input=-1
count=0
total=0

while user_input != "":
    user_input=input("Enter a number and nothing to calculate average:")
    if user_input.isdigit():
        total += int(user_input)
        count +=1
    

print(total /count)