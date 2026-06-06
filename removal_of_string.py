text = input("Enter any String : ")
char = input("What do you want to remove from the Entered String: ")
result =""
for i in text:
    if i !=char:
        result += i

print(f"The removed string :{char} after removal will be result :{result}")