#author:Arthur Drummond
#04/09/25
#Description:Program that asks weather conditions and responds accordingly
rainy=input("Is it raining?:").lower()
if ("yes" in rainy or "rain" in rainy):
    windy= input("is it windy?:").lower()
    if ("yes" in windy):
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")