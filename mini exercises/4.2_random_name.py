#100 Days of code with python
#Author: Mathias Nerd
#Choosing a random person to pay the bill
import random


entry = input("Give me everybody's names, separated by comma.\n")
entry_list = entry.split(", ")
#Generating a random number as the index
index = random.randint(0,len(entry_list) - 1)
print(f"{entry_list[index]} is going to buy the meal today!")