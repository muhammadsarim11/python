distance = float(input("Enter distance traveled (km): "))
fuel = float(input("Enter fuel used (liters): "))
consumption = distance / fuel
print("Fuel consumption:", round(consumption, 2), "km/l")