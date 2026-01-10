print("Hello! Welcome to Sam's Grocery Store!")
print( "\n We have a variety of items for you to choose from. \n")
print("""Menu: 
            1. Add a new item   

            2. Display the contents of the shopping cart

            3. Remove an item (only needed for the final project deliverable)

            4. Compute the total (only needed for the final project deliverable)

            5. Quit

""")
item_name=[]
item_price=[]
#ADD NEW ITEMS

while True:
    user_choice=int(input("Please enter your choice (1-5): "))
    if user_choice == 1:
        name=input("Enter the item name: ")
        price=float(input("Enter the item price: "))
        item_name.append(name)
        item_price.append(price)
        print(f"{name} has been added to your shopping cart at ${price:.2f}.\n")
    
    elif user_choice == 2:
        print("\nYour shopping cart contains the following items:")
        for i in range(len(item_name)):
            print(f"{i+1}. {item_name[i]} - ${item_price[i]:.2f}")
        print()
    
    elif user_choice == 3:
        item_to_remove=int(input("Enter the item number to remove: "))
        if 0 < item_to_remove <= len(item_name):
            removed_name = item_name.pop(item_to_remove - 1)
            removed_price = item_price.pop(item_to_remove - 1)
            print(f"{removed_name} has been removed from your shopping cart.\n")
        else:
            print("Invalid item number.\n")
    
    elif user_choice == 4:
        total=sum(item_price)
        print(f"The total cost of your shopping cart is: ${total:.2f}\n")
    
    elif user_choice == 5:
        print("Thank you for shopping with us! Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")


