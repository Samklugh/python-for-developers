#libraries are pre-written code that you can use to perform common tasks without having to write the code from scratch.
#Python has a rich ecosystem of libraries that can be imported and used in your programs.

#Importing a library
import math
#to know the functions in the math library, hit math. and see the suggestions

number = 16.23
rounded_up = math.ceil(number)  # Rounds up to the nearest integer
rounded_down = math.floor(number)  # Rounds down to the nearest integer

print(f"Original number: {number}, Rounded up: {rounded_up}, Rounded down: {rounded_down}")