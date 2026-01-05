payment= float(input("Enter the payment amount: "))

penalty= 0

while payment < 0:

    # penalty= 1.50 
    #this style of variable declaration is wrong. A variable belongs to the  body of code where it is used. its scope is limited to that body of code. instead, declare penalty outside the loop.
    penalty += 1.50
    print("Error: Payment amount cannot be negative.")

    payment= float(input("Enter the payment amount: "))

print(f"Payment amount accepted: ${payment:.2f}. A penalty of ${penalty:.2f} has been applied.")