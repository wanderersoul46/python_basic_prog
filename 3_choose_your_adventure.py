# Get the player's name
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

# Start the adventure with the initial choice
answer = input("You are on a dirt road that has come to an end. You can go left or right. Which way would you like to go? (left/right): ").lower()

# Check the first choice
if answer == "left":
    # If left, present another choice about a river
    answer = input("You come to a river. Do you want to walk around it or swim across? (walk/swim): ").lower()
    
    # Check the second choice about the river
    if answer == "swim":
        print("You swim across and were eaten by an alligator. You lose the game.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    # If right, present another choice about a bridge
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross or head back? (cross/back): ").lower()
    
    # Check the second choice about the bridge
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        # If crossing the bridge, present another choice about talking to a stranger
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to the stranger? (yes/no): ").lower()
        
        # Check the third choice about talking to the stranger
        if answer == "yes":
            print("You talk to the stranger and they give you Gold. You WIN!")
        elif answer == "no":
            print("You walked for many miles, ran out of water, and you lost the game.")
        else:
            print("Not a valid option. You lose.")

else:
    # If neither left nor right, it's an invalid option
    print("Not a valid option. You lose.")

# Display a closing message
print("Thanks for trying,", name)
