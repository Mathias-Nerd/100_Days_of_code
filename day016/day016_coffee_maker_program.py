from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


Coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

still_on = True



while still_on:
    options = menu.get_items()
    user_input = input(f"What would you like? {options}: ").lower()
    if user_input == "report":
        Coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        still_on = False
    else:
        drink = menu.find_drink(user_input)
        if drink:
            if Coffee_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost):
                Coffee_maker.make_coffee(drink)