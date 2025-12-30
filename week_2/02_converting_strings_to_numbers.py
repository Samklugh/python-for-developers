#converting strings to numbers

# length1 = 224
# length2 = 115
# length3 = input("Enter the length of the song in seconds: ")
# 
# song_duration= length1 + length2 + int(length3)
# print(f"The total song duration is {song_duration} seconds")
# 
# OR

length1 = 224
length2 = 115
length3 = int(input("Enter the length of the song in seconds in integers: "))
length4= float(input("Enter the length of the song in seconds in floats/decimals: "))

#note: input from user is always in string format, so we need to convert it to int or float before performing arithmetic operations

song_duration= length1 + length2 + length3 + length4
print(f"The total song duration is {song_duration} seconds")