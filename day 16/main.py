from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_is_on:
    print("Hello!")
    options = menu.get_items()
    user_choice = input(f"What would you like to drink? type: {options} :")
    if user_choice == "report":
        coffee_maker.report()
    elif user_choice == "stop":
        machine_is_on = False
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




