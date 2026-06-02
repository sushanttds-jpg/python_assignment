purchased_amount = float(input("Enter the purchased amount: "))

if purchased_amount >= 5000:
    discount_pct = 0.10
elif purchased_amount >= 4000: # implicitly less than 5000
    discount_pct = 0.07
elif purchased_amount >= 3000:
    discount_pct = 0.05
elif purchased_amount >= 2000:
    discount_pct = 0.03
else:
    discount_pct = 0.02
discount_amount = purchased_amount * discount_pct
final_price = purchased_amount - discount_amount
print(f"Discount: {discount_pct * 100}% (Rs. {discount_amount})")
print(f"Final Amount to Pay: Rs. {final_price}")
