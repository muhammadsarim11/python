file_size = float(input("Enter file size (MB): "))
speed = float(input("Enter internet speed (Mbps): "))
time_seconds = (file_size * 8) / speed
print("Download time:", round(time_seconds, 2), "seconds")