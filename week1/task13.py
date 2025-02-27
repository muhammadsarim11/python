item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
item4 = float(input("Enter price of item 4: "))
item5 = float(input("Enter price of item 5: "))
total = item1 + item2 + item3 + item4 + item5
if total > 100:
 discount = total * 0.05
 total -= discount
print("Final bill amount:", total)
