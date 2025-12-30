#area of a square
lenght = int(input("Enter the lenght of a square: "))
square_area = lenght * lenght
print(f"The area of the square is {square_area}")

#area of a rectangle
length = int(input("Enter the length of a rectangle: "))
width = int(input("Enter the width of a rectangle: "))
rectangle_area = length * width
print(f"The area of the rectangle is {rectangle_area}")

#area of a circle
import math
radius = float(input("Enter the radius of a circle: "))
circle_area = math.pi * radius ** 2
print(f"The area of the circle is {circle_area:.2f}")