"""Program to convert the seconds into hour, minutes and seconds."""
total_seconds = int(input("Enter the number in seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours} Hours : {minutes} Minutes : {seconds} Seconds")