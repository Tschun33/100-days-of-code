import math

import Menu
balance = 0
machine_is_running = True


def check_coins(penny, nickel, dime, quarter):
    sum_coins = round(penny * 0.01 + nickel * 0.05 + dime * 0.10 + quarter * 0.25, 2)
    return sum_coins


def check_price(sum_coins, price):
    if price > sum_coins:
        print("Not enough money!")
        return False
    else:
        return True


def print_resources():
    water = Menu.resources["water"]
    milk = Menu.resources["milk"]
    coffee = Menu.resources["coffee"]
    print(f"water: {water}, milk: {milk}, coffee: {coffee}")


def return_change(sum_coins, price):
    change = round(sum_coins - price, 2)
    print(f"Your change is: ${change}")


def check_resources(beverage, name):
    if beverage["ingredients"]["water"] > Menu.resources["water"]:
        print("Not enough water")
        return False
    if name == "latte" or name == "cappuccino":
        if beverage["ingredients"]["milk"] > Menu.resources["milk"]:
            print("Not enough milk")
            return False
    if beverage["ingredients"]["coffee"] > Menu.resources["coffee"]:
        print("Not enough coffee")
        return False
    else:
        return True


def make_beverage(beverage, name):
    new_water = Menu.resources["water"] - beverage["ingredients"]["water"]
    if name == "latte" or name == "cappuccino":
        new_milk = Menu.resources["milk"] - beverage["ingredients"]["milk"]
        Menu.resources["milk"] = new_milk
    new_coffee = Menu.resources["coffee"] - beverage["ingredients"]["coffee"]
    Menu.resources["water"] = new_water
    Menu.resources["coffee"] = new_coffee


while machine_is_running:
    choice = input("Espresso Cappuccino or Latte ?")
    choice = choice.lower()
    if choice == "latte" or choice == "cappuccino" or choice == "espresso":
        choice_customer = Menu.MENU[choice]
        if check_resources(choice_customer, choice):
            penny_count = int(input("Pennies:"))
            nickel_count = int(input("Nickels:"))
            dime_count = int(input("Dimes:"))
            quarter_count = int(input("Quarters:"))
            coin_sum = check_coins(penny_count, nickel_count, dime_count, quarter_count)
            print(f"The total value is ${coin_sum}")
            if check_price(coin_sum, choice_customer["cost"]):
                balance += choice_customer["cost"]
                make_beverage(choice_customer, choice)
                return_change(coin_sum, choice_customer["cost"])
                print(f"The balance is: ${balance}")
    elif choice == "report":
        print_resources()
    elif choice == "stop":
        machine_is_running = False
    else:
        print("no valid input")


