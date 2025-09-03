#author:Arthur Drummond
#02/09/25
#Description:Program that converts cm to feet and inches

heightCm=float(input("What is your height in cm:"))
inchesTotal=heightCm/2.54
feet=inchesTotal//12
feet =int(feet)
inches = int(inchesTotal % 12)

print(feet,",",inches)