# Welcome message
print("Welcome to play the quiz!")

# Ask the player if they want to play
player = input("Do you want to play?")

# If the player's response is not 'yes', quit the game
if player.lower() != "yes":
    quit()

# Start the game
print("Ok, let's play!")

# Initialize the score
score = 0

# Ask the first question
question = input("How many days do we have in a week? ")
# Check if the answer is correct and update the score
if question.lower() == "seven":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Ask the second question
question = input("In which direction does the sun rise? ")
# Check if the answer is correct and update the score
if question.lower() == "east":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Ask the third question
question = input("What is our national bird? ")
# Check if the answer is correct and update the score
if question.lower() == "peacock":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Ask the fourth question
question = input("What is the fastest animal on land? ")
# Check if the answer is correct and update the score
if question.lower() == "cheetah":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Ask the fifth question
question = input("What is the largest ocean in the world? ")
# Check if the answer is correct and update the score
if question.lower() == "pacific ocean":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Display the final score
print(f"Your score: {score}")
