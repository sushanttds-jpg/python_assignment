x = ["Data Science", "Computer Science"]
y = ["Data Science", "Computer Science"]
z = x

# Membership Operators
print("Data Science" in x) # True [11]
print("Scientist" not in x) # True [11]

# Identity Operators 
print(x is z) # True, z is the same object as x [13]
print(x is y) # False, they have same content but are different objects [13]