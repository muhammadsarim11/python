# task 5

seconds = int(input("Enter seconds to convert: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remainig_seconds = seconds % 60

print("hours: ", hours, "minutes: ",minutes,"remainig_seconds",remainig_seconds)
