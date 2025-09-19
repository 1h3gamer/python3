units = int(input("Enter the units consumed: "))

if units <= 50:
    amount= units * 2.60
    surcharge = 25
elif units <= 100:
    amount = (50 * 2.60) + (units - 50) * 3.25
    surcharge = 35
elif units <= 200:
    amount = (50 * 2.60) + (50 * 3.25) + (units - 100) * 5.26
    surcharge = 45
else:
    amount = (50 * 2.60) + (50 * 3.25) + (50 * 5.26) + (units - 200) * 8.25
    surcharge = 75

print(f"Electricity bill= {amount + surcharge :.2f}")
