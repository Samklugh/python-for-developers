#avoid putting different variable types in the same list

points_scored = [10, 20, 15, 30, 25]  # List of integers representing points scored in different games

runnin_total = 0  # Initialize running total to zero

for points in points_scored:
    runnin_total += points  # Add each game's points to the running total

print("Total points scored:", runnin_total)  # Print the total points scored