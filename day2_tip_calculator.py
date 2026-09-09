#Day 2 of 100 days of code with python
#Author: Mathias Nerd
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num = int(input("How many people to split the bill? "))
tip = bill * ( percent / 100 )
calc = ( bill + tip ) / num
print(f"Each person should pay: {round(calc,2)}")
