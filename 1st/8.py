randNoDays= input("Enter a random number of days:")
randNoDays = int(randNoDays)
if randNoDays ==(1):
    print("There are",randNoDays*24,"hours,", randNoDays*1140,"minutes,","and",randNoDays*86400,"seconds in",randNoDays,"day")
elif randNoDays<1:
    print("Can't have minus days")
else:
    print("There are",randNoDays*24,"hours,", randNoDays*1140,"minutes,","and",randNoDays*86400,"seconds in",randNoDays,"days")