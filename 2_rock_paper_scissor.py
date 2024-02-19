import random

# Initialize counters for user and computer wins
User_wins = 0
computer_wins = 0

# Define the options for the game
options = ["rock", "paper", "scissor"]

# Main game loop
while True:
    # Get user input
    user_input = input("Type rock/paper/scissor or q to quit: ").lower()

    # Check if the user wants to quit
    if user_input == "q":
        break

    # Check if the user input is valid
    if user_input not in options:
        continue

    # Generate a random choice for the computer
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked:", computer_pick + ".")

    # Determine the winner of the round
    if (
        (user_input == "rock" and computer_pick == "scissor")
        or (user_input == "paper" and computer_pick == "rock")
        or (user_input == "scissor" and computer_pick == "paper")
    ):
        print("You won!")
        User_wins += 1
    elif (
        (user_input == "scissor" and computer_pick == "rock")
        or (user_input == "rock" and computer_pick == "paper")
        or (user_input == "paper" and computer_pick == "scissor")
    ):
        print("You lost!")
        computer_wins += 1
    else:
        print("It's a tie!")

# Display the final results
print("You won", User_wins, "times")
print("Computer won", computer_wins, "times")

print("Goodbye!")
