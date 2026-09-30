#Rock paper scissors
import random

options = ["rock", "paper", "scissors"]

still_playing = True

while still_playing:
    computer = random.choice(options)
    user = input("Enter rock, paper, scissors or q to quit: ").lower()
    if user == "q":
        break
    print(f"Player: {user}")
    print(f"Computer: {computer}")
    match (computer, user):
        case (computer, user) if computer == user:
            print("Draw")
        case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            print("Computer wins!")
        case ("scissors", "rock") | ("rock", "paper") | ("paper", "scissors"):
            print("You win")
        case _:
            print("Wrong input")
            continue
    




    