scripture= "Rejoice evermore."

for letter in scripture:
    print(letter)

# OR
#when the length is unknown, we use the below code:

for i in range(17):
    letter = scripture[i]
    print(letter)

# OR
# we can also use len() function to get the length of the string

scriptutre_length = len(scripture)

for i in range(scriptutre_length):
    letter = scripture[i]
    print(letter)

# OR
# we can combine the above two steps into one line
for i in range(len(scripture)):
    letter = scripture[i]
    print(letter)