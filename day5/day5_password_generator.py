#100 Days of code with python
#Author: Mathias Nerd
#Py password generator
import random

#The letters, numbers and symbols variable so that we can pick randomly
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword generator!")
letter_length = int(input("How many letters would you like in your password?\n"))
sym_length = int(input("How many symbold would you like?\n"))
num_length = int(input("How many numbers would you like?\n"))

result_list = []

#Loop for putting random letters into the list
for i in range(0, letter_length):
    result_list.append(random.choice(letters))
#Loop for putting random numbers into the list
for j in range(0, sym_length):
    result_list.append(random.choice(numbers))
#Loop for putting random symbols into the list
for k in range(0, num_length):
    result_list.append(random.choice(symbols))


random.shuffle(result_list) #Shuffling the result_list
result = "".join(result_list)
print(f"Here is your password: {result}") 