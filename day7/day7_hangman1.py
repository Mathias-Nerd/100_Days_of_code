#100 Days of Code
#Author: Mathias Nerd
#Hangman game
import random
import hangman_names
import hangman_art


word_list = hangman_names.names
stages = hangman_art.stages
logo = hangman_art.logo

rand_word = random.choice(word_list)
word_length = len(rand_word)
print(logo)
#For testing code
# print(f"The solution is {rand_word}.")

lives = 6
#The empty list that will be filled
display = []
for letter in rand_word:
    display.append('_')
print(display)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You have already guessed {guess}") 
    for ch in range(word_length):
        if guess == rand_word[ch]:
            display[ch] = guess
    print(display)
        
    
    if guess not in rand_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(stages[-lives])
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    

    if "_" not in display:
        end_of_game = True
        print("You win")
