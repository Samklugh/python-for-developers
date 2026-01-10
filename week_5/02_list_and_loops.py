clients=[]
new_clients=""
while new_clients.lower() != "quit":
    new_clients = input("Enter client names (or type 'quit' to finish): ")
    if new_clients.lower() != "quit":
        clients.append(new_clients)


for client in clients:
    print("Client Name:", client)