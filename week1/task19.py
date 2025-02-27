speed_limit = float(input("Enter speed limit (km/hr): "))
actual_speed = float(input("Enter actual speed (km/hr): "))
if actual_speed > speed_limit:
 fine = (actual_speed - speed_limit) * 10
 print("You are fined: $", fine)
else:
 print("No fine, you are within the speed limit.")