# task 8

original_price = float(input("ENter the original price"))
discount_percent = float(input("Enter the discount price"))

discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount
print("final price is ",final_price)
