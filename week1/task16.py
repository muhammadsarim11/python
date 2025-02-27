bill_amount = float(input("Enter bill amount: "))
tip_percentage = float(input("Enter tip percentage: "))
tip = (bill_amount * tip_percentage) / 100
print("Tip amount:", tip)
print("Total amount to pay:", bill_amount + tip)