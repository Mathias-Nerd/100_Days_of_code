#100 Days of code with python
#Author: Mathias Nerd
#Treasure Island

# RULES - TREASURE ISLAND:
# 1. Start at crossroad -> must go 'left' to continue, 'right' = lose
# 2. At lake -> must 'wait' for boat, 'swim' = lose  
# 3. At house with 3 doors -> 'red' = fire (lose), 'blue' = beasts (lose), 'yellow' = treasure (win)
# 4. All choices .lower() and any other input = Game Over

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' \n")
if choice1 == "left":
    choice2 = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for boat. Type 'swim' to swim across \n")
    if choice2 == "swim":
        print("game over.")
    else:
        choice3 = input("You arrived at the island unharmed. THere is a house with 3 doors. One red, and yellow and one blue. Which colour do you choose?")
        if choice3 == "red":
            print("You just entered into fire, game over.")
        elif choice3 == "blue":
            print("You just entered a room with a beast, game over.")
        elif choice3 == "yellow":
            print("You just found the treasure, You win")
elif choice1 == "right":
    Print("You lose")
else:
    print("Wrong input")