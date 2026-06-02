n = int(input("Enter a number: "))
print("palindrome" if str(n) == str(n)[::-1] else "not palindrome")