#100 Days of code with python
#Author: Mathias Nerd
#Using random number to randomly toss a coin
import random #importing the random module


random_num = round(random.random()) #generating a random number and rounding it up to integers
print("Head" if random_num == 1 else "Tail")