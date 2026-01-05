groceries= ['apples', 'bananas', 'carrots', 'dates', 'eggs', 'flour', 'grapes']

for item in groceries:
    print(f"the item is: {item} and cost is on the tag.")
    for char in item:
        print(f"   character: {char}")

for i in range (5):
    print(f"i is now: {i}")
    for k in range (10, 15):
        print(f"     k is : {k}")