x = float(input("Enter value of x: "))
n = int(input("Enter value of n: "))

s = 1

for i in range(1, n + 1):
    term = i * (x ** i)

    if i % 2 == 0:      
        s -= term
    else:               
        s += term

print("Sum =", s)