
#comparing numbers

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

if num1 > num2:
    print("{} is greater than {}".format(num1, num2))

elif num1 == num2:
    print("{} is equal to {}".format(num1, num2))

else:
    print("{} is less than {}".format(num2, num1))


#comparing strings

my_favorite_animal= "dog"
user_animal= input("Enter your favorite animal: ").lower()

if my_favorite_animal == user_animal:
    print("This is my favorite animal: {}".format(user_animal))

else:
    print("This is not my favorite animal: {}".format(user_animal))