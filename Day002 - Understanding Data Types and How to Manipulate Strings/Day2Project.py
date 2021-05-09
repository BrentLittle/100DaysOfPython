### Tip Calculator ###

print("Welcome to the Tip Calculator")
billTotal = float(input("What was the Bill total? $"))
tipPercentage = int(input("What Tip Percentage would you like to give? "))
numPeople = int(input("How many people will be splitting the bill? "))

totalWithTip = billTotal + ( billTotal * (tipPercentage/100))
billSplitEqual = round(totalWithTip / numPeople, 2)

print(f"Each person should pay: ${billSplitEqual}")