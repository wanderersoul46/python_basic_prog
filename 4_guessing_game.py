import random

def guess_the_number():
    # Welcome message
    print("Welcome to the Number Guessing Game!")

    # Set the lower and upper bounds for the secret number
    lower_bound = 1
    upper_bound = 100

    # Generate a random secret number within the specified bounds
    secret_number = random.randint(lower_bound, upper_bound)

    # Initialize the attempts counter
    attempts = 0

    # Display the range of possible numbers
    print(f"Guess the number between {lower_bound} and {upper_bound}")

    # Main game loop
    while True:
        # Get user input for their guess
        user_guess = input("Enter your guess: ")

        # Check if the input is a valid number
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        # Convert user input to an integer
        user_guess = int(user_guess)
        attempts += 1

        # Check the user's guess against the secret number
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Call the function to start the game
guess_the_number()
