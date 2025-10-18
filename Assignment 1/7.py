#author:Arthur Drummond
#02/09/25
#Description:Program calcs how much each diner has to pay

totalBill= input("What is the total bill:")
totalBill= float(totalBill)
numberOfDiners = input("How many diners were there:")
numberOfDiners= int(numberOfDiners)
print("Each person must pay",totalBill/numberOfDiners,"$")