total=0

for i in range(1,6):
    num=float(input("Enter a number:"))
    q=input("Type yes if you wish to add it to the total:").lower()
    if "yes" in q:
        total+=num
print("The total is",total)