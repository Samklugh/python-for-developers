
print("Welcome to the word guessing game!")
secret_word = "grace" 
secret_word = secret_word.lower()

# Generate initial hint (all underscores)
hint = "_ " * len(secret_word)
print("\nYour hint is:", hint)

guess_count = 0
guess = ""

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    # Check if guess length matches
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
        continue 

    # Check for alphabetic only (creative feature)
    if not guess.isalpha():
        print("Warning: Please enter letters only. Non-alphabetic characters detected.\n")
        continue

    # Build the hint
    new_hint = ""

    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:

            # Correct letter in correct position
            new_hint += guess[i].upper() + " "
        elif guess[i] in secret_word:
            # Correct letter but wrong position
            new_hint += guess[i].lower() + " "
        else:
            # Letter not found in secret word
            new_hint += "_ "

    # Display hint (unless correct guess)
    if guess != secret_word:
        print("Your hint is:", new_hint)

# Correct guess reached
print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
