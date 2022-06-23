from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_is_on:
    print("Hello!")
    user_choice = input("What would you like to drink? type: cappuccino, espresso or latte:")
    if user_choice == "cappuccino" or user_choice == "espresso" or user_choice == "latte":
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    elif user_choice == "report":
        coffee_maker.report()



