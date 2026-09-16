#100 Days of code with python
#Author: Mathias Nerd
#Pizza delivery

print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
pep_price = 0

if size == 'S':
    price = 15
    if add_pepperoni == 'Y':
        pep_price = 2
elif size == 'M':
    price = 20
    if add_pepperoni == 'Y':
        pep_price = 3
elif size == 'L':
    price = 25
    if add_pepperoni == 'Y':
        pep_price = 3
else:
    print("Invalid size entered")

amt = price + pep_price + (1 if  extra_cheese == 'Y' else 0)


print(f"Your final bill is: ${amt}")