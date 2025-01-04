print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go?")
first_choice = input("Type 'left' or 'right' ").lower()
if first_choice == "right":
    print("You fell into a hole. Game Over.")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    second_choice = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if second_choice == "swim":
        print("You were attacked by trout. Game Over.")
    else:
        print("You've arrived at the island unharmed. There is a house with three doors.")
        third_choice = input("One red, one yellow and one blue. Which color do you choose? ").lower()
        if third_choice == "blue":
            print("You were eaten by beasts. Game Over.")
        elif third_choice == "red":
            print("You got burned by fire. Game Over.")
        elif third_choice == "yellow":
            print("Congratulations! You won!")
        else:
            print("Invalid choice. Game Over.")
