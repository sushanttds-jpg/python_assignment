a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b:
    if a > c:
        print(f"{a} is the largest number.")
    else:
        print(f"{c} is the largest number.")
else:
    if b > c:
        print(f"{b} is the largest number.")
    else:
        print(f"{c} is the largest number.")