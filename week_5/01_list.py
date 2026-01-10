#list is the collection which is ordered and changeable. Allows duplicate members. 
#list is written with square brackets.
# thislist = ["apple", "banana", "cherry"]

clients= []

clients.append("John")
clients.append("Alice")

# print(clients)

new_clients = []

names= input("Enter client names separated by commas: ")
new_clients.append(names)
print(new_clients)

for client in new_clients:
    print("Client Name:", client)