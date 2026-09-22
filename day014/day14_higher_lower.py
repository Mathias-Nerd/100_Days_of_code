#100 Days of Code
#Author: Mathias Nerd
#Higher lower game

#Import the ascii module
import art
import random
import game_data
from replit import clear
#First display the ascii art

data = game_data.data
logo = art.logo
vs = art.vs
clear()
print(logo)


#personA: pick a rando person
#create a function play_game()
def play_game():
    personA = random.choice(data)
    data.remove(personA)
    still_playing = True
    score = 0
    while still_playing:
        # print(personA)
        print(f"Compare A: {personA["name"]}, a {personA["description"]}, from {personA["country"]}")
        print(vs)
        personB = random.choice(data)
        data.remove(personB)

        # print(personB)
        print(f"Against B: {personB["name"]}, a {personB["description"]}, from {personB["country"]}")
        guess = input("Who has more followers 'A' or 'B': ").upper()
        if guess == 'B':
            res = personB["follower_count"] > personA["follower_count"]
        elif guess == 'A':
            res = personA["follower_count"] > personB["follower_count"]
        clear()
        print(logo)

        if res:
            score += 1
            print(f"You are right. Current score: {score}")
            personA = personB
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            still_playing = False
      




play_game()
#   a var still_playing = True
#   get a random