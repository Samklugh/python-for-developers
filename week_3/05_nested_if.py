rewards = 0
choice = "drinks"
total_order = 20

if (choice == "drinks" or choice == "cookie") and total_order >= 5:
    rewards += 5

print(f"You have earned {rewards} rewards points")