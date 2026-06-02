bs_year = int(input("Enter B.S. Year: "))
bs_month = int(input("Enter B.S. Month (1-12): "))
bs_day = int(input("Enter B.S. Day: "))
ad_year = bs_year - 56
ad_month = bs_month - 8
ad_day = bs_day - 15
if ad_day <= 0:
    ad_month -= 1
    ad_day += 30 # Rough approximation for a month
if ad_month <= 0:
    ad_year -= 1
    ad_month += 12 
print(f"Estimated A.D. Date: {ad_year}-{ad_month:02d}-{ad_day:02d}")