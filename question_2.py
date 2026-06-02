"""Write a python program to find the gpa according to the criteria implemented in Data Science
(BDS) using logical and operators."""
calc = float(input("Enter your Gpa in calculus : "))
alzeb = float(input("Enter your Gpa in alzebra : "))
pyth = float(input("Enter your Gpa in python programming: "))
Database = float(input("Enter your Gpa in data base: "))
stats = float(input("Enter your Gpa  in statistics: "))
total = (calc + alzeb + pyth + Database + stats) /5
print("***calculating your Gpa ****")
if total >= 3.70:
    print("you Got A")
elif total >= 3.30 and total  <=3.70:
    print("you Got A-")
elif total >=3.0 and total <=3.29:
    print("you Got B+")
else:
    print("you Got below B")


