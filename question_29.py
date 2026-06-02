products = [
    {'name': 'Milk', 'expiration_date': 'tomorrow', 'price': 50.0},
    {'name': 'Bread', 'expiration_date': 'today', 'price': 100.0}
]
for product in products:
    if product['expiration_date'] != 'today':
        continue 
    product['price'] *= 0.8 
    print(f"Discounted {product['name']}: Rs.{product['price']}")
attempts = 0
while True:
    password = input("Enter password: ")
    if password == "secret123":
        print("Access Granted!")
        break 
    attempts += 1
    if attempts == 3:
        print("Account Locked!")
        break 