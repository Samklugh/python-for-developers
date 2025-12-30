#get users details

price_for_child =float(input("Enter the price for a child's meal: "))
price_for_adult =float(input("Enter the price for an adult's meal: "))
number_of_children =int(input("Enter the number of children: "))
number_of_adults =int(input("Enter the number of adults: "))

#subtotal calculation
subtotal = (price_for_child * number_of_children) + (price_for_adult * number_of_adults)
print(f"Subtotal: ${subtotal:.2f}")

# taxes calculation
sales_tax_rate = float(input("Enter the sales tax rate (not less than 0): ")) 

#sales tax amount
sales_tax_amount = subtotal * (sales_tax_rate / 100)

#total meal cost with tax
total_meal_cost = subtotal + sales_tax_amount

#payment and change calculation
payment_amount = float(input("Enter the amount you want to pay: "))
change_due = payment_amount - total_meal_cost
print(f"Change due: ${change_due:.2f}")