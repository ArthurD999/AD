#Arthur Drummond
#2/10/25
#A program that averages inputed grades and prints letter grade

count=0
total=0
user=1
while user > 0:
    user_input=input("Enter your grades:")
    if user_input.isdigit():
        user_input=int(user_input)
        if user_input > 0:
            total += int(user_input)
            count +=1
    else:
        user = -1
             
             
             
if total/count > 90:
    print("A")

elif total/count > 80:
    print("B")

elif total/count > 70:
    print("C")
    
elif total/count > 60:
    print("D")

elif total/count > 50:
    print("E")

elif total/count > 40:
    print("F")
