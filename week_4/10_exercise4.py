import random

keep_playing = 'yes'
while keep_playing == 'yes':

    secret_number = random.randint(1, 100)
    # print(f"the random number is: {secret_number}")  # For testing purposes; remove in production
    guess_count = 0
    guess = -1

    while guess != secret_number:
        guess= int(input("Enter your guess number: "))
        guess_count += 1
        if guess < secret_number:
            print("Too low! Guess higher.")

        elif guess > secret_number:
            print("Too high! Guess lower.")
        else:
            print("Congratulations! You've guessed the correct number.")

    print(f"It took you {guess_count} guesses.")

    keep_playing = input("Do you want to play again? (yes/no): ").strip().lower()