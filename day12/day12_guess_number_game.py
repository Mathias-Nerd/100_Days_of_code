#100 Days of Code
#Author: Mathias Nerd
#Day 12: Guess Number game


#Import the random module so that you canuse it to get a random number 
import random

print("Welcome to a guess number game!\nI'm thinking of a number between 1 and 100.")
#Tha variable reading the difficulty level
diff_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

match diff_level:
    case "easy":
        attempt = 10
    case "hard":
        attempt = 5
    case _:
        print("You entered a wrong difficulty level")

def play_game(attempt):
    random_number = random.randrange(1, 101)
    while attempt >= 1:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer is {guess}.")
            break
        if guess >= random_number:
            print("Too high.")
        else:
            print("Too low.")
        attempt -= 1
        print("Guess again" if attempt >= 1 else f"You've run out of guesses, you lose.") 

play_game(attempt)


