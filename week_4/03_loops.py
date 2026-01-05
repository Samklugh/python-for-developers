number= 0 # initialize the variable that is of number data type. any number can be used provided that it is less than the condition in the while loop.

name= " " # initialize the variable that is of string data type. an empty string is used here.
while number < 5:

    number = int(input("Enter a number greater than or equal to 5: "))
    name = input("Enter your name: ")

print(f"Thank you! You entered: {number} and your name is {name}.")