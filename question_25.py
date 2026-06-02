monthly_gross = 125000
yearly_gross = monthly_gross * 12 
tax = 0
if yearly_gross <= 500000:
    tax = yearly_gross * 0.01
elif yearly_gross <= 700000:
    tax = (500000 * 0.01) + ((yearly_gross - 500000) * 0.10)
elif yearly_gross <= 1000000:
    tax = (500000 * 0.01) + (200000 * 0.10) + ((yearly_gross - 700000) * 0.20)
elif yearly_gross <= 2000000:
    # 1.5M falls in this bracket!
    tax = (500000 * 0.01) + (200000 * 0.10) + (300000 * 0.20) + ((yearly_gross - 1000000) * 0.30)
elif yearly_gross <= 5000000:
    tax = (500000 * 0.01) + (200000 * 0.10) + (300000 * 0.20) + (1000000 * 0.30) + ((yearly_gross - 2000000) * 0.36)
else:
    tax = (500000 * 0.01) + (200000 * 0.10) + (300000 * 0.20) + (1000000 * 0.30) + (3000000 * 0.36) + ((yearly_gross - 5000000) * 0.39)
yearly_net = yearly_gross - tax
monthly_net = yearly_net / 12
print(f"Yearly Gross: Rs. {yearly_gross}")
print(f"Yearly Tax Deducted: Rs. {tax}")
print(f"Exact Monthly Net Salary: Rs. {monthly_net:.2f}")