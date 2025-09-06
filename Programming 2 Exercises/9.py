#author:Arthur Drummond
#06/09/25
#Description:Program that calculates water bill based on units entered and band rates
units_used=int(input("Enter how many units of water were used:"))
if units_used < 100:
    band_1 = (0.05*units_used)
    print(band_1,"$")
if units_used >100 and units_used <250:
    band_1 = ((units_used-100)*0.1)+0.05*100
    print(band_1,"$")
if units_used > 250:
    band_1 = ((units_used-250)*0.2) + 100*0.05+0.1*150
    print("Water bill is",band_1,"$")
