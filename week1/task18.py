weight = float(input("Enter weight in kg: "))
duration = float(input("Enter exercise duration (minutes): "))
MET = float(input("Enter MET value of activity: "))
calories_burned = (MET * weight * duration) / 60
print("Calories burned:", round(calories_burned, 2))