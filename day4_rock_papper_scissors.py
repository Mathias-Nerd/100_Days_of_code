#100 Days of code with python
#Author: Mathias Nerd
#Rock Paper Scissors game
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
possible_choices = ["rock", "paper", "scissors"]
print("Welcome to rock, paper, scissors game\n")

#Receiving player input
player_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))
print("You chose")
print(rock if player_choice == 1 else paper if player_choice == 2 else scissors)
#Setting the choice
player_value = possible_choices[player_choice - 1]


#randomly generating computer's input
computer_choice = random.randint(1,3)
#Setting the choice
computer_value = possible_choices[computer_choice - 1]
print("Computer chose")
print(rock if computer_choice == 1 else paper if computer_choice == 2 else scissors)

#Joining both choices
res = player_value + computer_value
print(res)

#The conditional part
match res:
    case ("rockscissors" | "scissorspaper" | "paperrock"):
        print("You win!")
    case ("scissorsrock" | "paperscissors" | "rockpaper"):
        print("You lose!")
    case _:
        print("It is a tie!")
