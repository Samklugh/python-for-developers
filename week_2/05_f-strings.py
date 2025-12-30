#format specifiers / f-strings

money = 1500.5678
print(f"Available balance: ${money:.2f}")  # Output: Available balance: $1500.57

#the :.2f inside the curly braces is a format specifier that tells Python to format the number as a float with 2 decimal places.

number = round(money, 2)
print(number)  # Output: 1500.57