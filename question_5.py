n = int(input("Enter a number  :"))
rem = []
while n>0:
    rems = n%2
    rem.append(rems)
    n=n//2
rem = rem[::-1]
print("In binary form:",rem)