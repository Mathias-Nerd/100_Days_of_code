#100 Days of Code
#Author : Mathias
#The secret aunction program



import os
import art

def clear_screen():
    # 'nt' is for Windows, 'posix' is for Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def find_max(dict):
    max_bid = 0
    for item in dict:
        if dict[item] > max_bid:
            max_bid = dict[item]
            max_name = item
    print(f"The winner is {max_name} with the bid of {max_bid}")

print(art.logo)
people_dict = {}
keep_running = True
while keep_running:
    name = input("Enter your name: ")
    bid = int(input("Enter bid: &"))
    people_dict[name] = bid
    choice = (input("Enter 'yes' if there are other users who want to bid else enter 'no' ? \n"))
    if choice == "yes":
        clear_screen()
    elif  choice == 'no':
        keep_running = False
        clear_screen()
        find_max(people_dict)