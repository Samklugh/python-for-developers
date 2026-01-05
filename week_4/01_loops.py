payment= float(input("Enter the payment amount: "))

while payment < 0: 
    print("Error: Payment amount cannot be negative.")
    payment= float(input("Enter the payment amount: "))
print(f"Payment amount accepted: ${payment:.2f}")