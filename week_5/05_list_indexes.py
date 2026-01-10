#list indexes start at 0
colors = ["red", "green", "blue", "yellow", "blue"]  # List of color names
# print("First color:", colors[0])  # Access and print the first color

for color in colors:
    print("Color:", color)  # Print each color in the list


    # OR

for i in range(len(colors)):
    print("Color at index", i, "is", colors[i])  # Print color at each index

    # OR 

    print(f"Color at index {i} is {colors[i]}")  # Using f-string for formatted output

    # OR 

    human_count= i + 1
    print("Color code " + str(human_count) + " is " + colors[i])  # Using string concatenation


    #.pop() removes and returns the last item in the list
last_color = colors.pop()
colors.pop(0)  # removes first item in the list
print("Removed color:", last_color)  # Print the removed color

#.insert() adds an item at a specific index
colors.insert(1, "orange")  # Insert "orange" at index 1
print("Colors after insertion:", colors)  # Print the updated list of colors

#.remove() removes the first occurrence of a specific value
colors.remove("blue")  # Remove "blue" from the list
