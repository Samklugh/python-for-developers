def welcome_message(name): #we added a parameter to personalize the welcome message.
    """the function prints a welcome message to the user."""
    print(f"Welcome {name} to the Python programming world!")

user=input("Please enter your name: ")  #getting user's name as input outside the function.
welcome_message(user)  #passing the user's name as an argument to the function to display a personalized welcome message. cvdff