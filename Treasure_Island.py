print("Welcome to Treasure Iceland")
print("Your Mission is to find the treasure")
choice1=input('you\'re at a cross road.Where do you want to go? Type "left" or "right".')

if choice1=="left":
    choice2=input('you have come to a lake.\nThere is an island in the middle of the lake.\n Type "wait" to wait for a boat.\n Type "swim" to swim across.').lower()
    if choice2=="wait":
        choice3=input("you arrive at the island unharmed.\n There is house with 3 doors. one red, one yellow and one blue. \nwhich colour do you choose?").lower()
        if choice3=="red":
            print("it's a room full of fire. Game over.")
        elif choice3=="yellow":
            print("you found the treasure. you win!")
        elif choice3=="blue":
            print("you enter a room of beasts. Game Over")
        else:
            print("you choose a door that doesn't exist. Game Over")
    else:
            print("you got attacked by an angry trout.Game Over")
else:
    print('You fell in to the hole. Game Over.')