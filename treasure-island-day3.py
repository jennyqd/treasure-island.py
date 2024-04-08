print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("What direction do you want to go? (Type 'left' or 'right') ").lower()

if direction == "left":
    action = input("Do you want to swim or wait? ").lower()
 
    if action == "wait":
        door = input("Which door do you want to go through? red, blue, or yellow? ").lower()

        if door == "red":
            print("You spontaneously combusted. GAME OVER")
        elif door == "blue":
            print("A horde of bloodthirsty beasts devoured you and wiped your very soul from existence. GAME OVER")
        elif door == "yellow":
            print("Yay! You found the treasure! You win!")
        else:
            print("GAME OVER")

    else:
        print("You were attacked by a mutant trout. GAME OVER")

else:
    print("You fell into a hole. GAME OVER")







