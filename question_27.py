import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = (b**2) - (4*a*c) 
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Two Real Roots: {root1:.2f} and {root2:.2f}")
elif d == 0:
    root1 = -b / (2*a)
    print(f"One Real Root: {root1:.2f}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-d) / (2*a)
    print(f"Imaginary Roots: {real_part:.2f} + {imaginary_part:.2f}j and {real_part:.2f} - {imaginary_part:.2f}j")