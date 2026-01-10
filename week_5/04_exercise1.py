friends= []

friend_name=""

while friend_name!="end":
    friend_name=input("Enter a friend's name (or 'end' to finish): ")
    friends.append(friend_name)

for name in friends:
    print("Hello, " + name + "!")