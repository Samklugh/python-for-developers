# common mistake 1. 
# Using 'or' incorrectly in conditional statements.
# x==4 or 6 is not the same as x==4 or x==6

x=int(input("Enter a number: "))
if x==4 or 6: # This expression is incorrect because it always evaluates to True. because 'or 6' is always True. even if x is not 4. because 6 is a truthy value. a truthy value is any value that is considered true in a boolean context. e.g. non-zero numbers, non-empty strings, etc.  
    print("x is 4 or 6")
else:
    print("x is not 4 or 6")
# This expression is incorrect because it does not check if x is equal to 4 or 6 properly.
# The correct way to write this expression is:
y=int(input("Enter a number: "))
if y==4 or y==6:
    print("y is 4 or 6")
else:
    print("y is not 4 or 6")


#commn mistake 2.
# string is not same as numnbers

age= input("Enter your age: ") # input() function returns a string

if age ==18: # This expression is incorrect because age is a string and 18 is an integer. so they are not the same type. so the comparison will always be False.
    print("You are 18 years old")
else:
    print("You are not 18 years old")


#common mistake 3.
#forgeting order of operations in conditional statements

rewards=0
choice= "drinks"
total_order=3

if choice=="drinks" or choice=="cookie" and total_order >=5:
    rewards +=5  #this would work incorrectly because of order of operations. 'and' has higher precedence than 'or'. so the expression would be evaluated as: choice=="drinks" or (choice=="cookie" and total_order >=5). so if choice is "drinks", the expression would be True regardless of total_order.
print(f"you have earned {rewards} rewards points")

# The correct way to write this expression is:

sam = 0
choices = "drinks"
total_orders = 3

# The condition checks:
# (choices == "drinks" or choices == "cookie") AND total_orders >= 5# So even if choices is valid, total_orders must be at least 5.

if (choices == "drinks" or choices == "cookie") and total_orders >= 5:
    sam += 5
    print(f"you have earned {sam} reward points")