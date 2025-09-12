actual_cost=float(input("Enter the actual cost"))
sale_amount=float(input("Enter the sale amount"))

if (sale_amount > actual_cost):
    amount= sale_amount - actual_cost
    print(amount)
else:
    print("No profit")