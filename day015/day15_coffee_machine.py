#100 Days of Code
#Author: Mathias Nerd
#A coffee Machine



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

#Putting the names of the rink in a list
drinks = []
for item in MENU:
    drinks.append(item)
print(drinks)


#The function that checks if resource is sufficienct
def check_resource_sufficiency(drink):
    for item in resources:
        if drink["ingredients"][item] >= resources[item] :
            print(f"Sorry there is not enough {item}.")
            return False
    return True

#The function that checks if money is enough
def transation_success(drink_cost, payment):
    if payment >= drink_cost:
        global profit
        profit += drink_cost
        if payment > drink_cost:
            print(f"Here is ${round(payment-drink_cost, 2)} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False 


#The function that receives coin 
def insert_coin():
    print("Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? "))   * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


#The function that dducts igredients
def make_coffee(drink, user_input):
    ingr = drink['ingredients']
    for item in ingr:
        global resources
        resources[item] -= ingr[item]
    print(f"Here is your {user_input}. Enjoy!")


#Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​
still_playing = True
while still_playing:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        still_playing = False
    elif user_input == "report":
        print(f"Water:  {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee {resources['coffee']}g")
        print(f"Money: ${profit}.")
    elif user_input in drinks:
        drink = MENU[user_input]
        cost = drink["cost"]
        if check_resource_sufficiency(drink):
            payment = insert_coin()
            if transation_success(cost, payment):
                make_coffee(drink, user_input)
                
    else:
        print("You entered a wrong choice.")