#Arthur Drummond
#10/09/25
# A program that prints takes multiple user inputs and user presses q to indicate finished
even = 0
odd = 0

done="y"
while done != "q":
    entered=(input("Enter a number or press q in done:"))
    if entered.isdigit():
        entered=int(entered)
        if entered % 2 == 0:
            even= even+1
        if entered % 2 == 1:
            odd = odd +1
    
    if entered == "q":
        done = "q"
    

print("Even:",even)
print("Odd:",odd)