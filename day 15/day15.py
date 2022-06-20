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
    change = sum_coins - price
    print(f"Your change is: ${change}")


def check_resources(beverage):
    if beverage["ingredients"]["water"] > Menu.resources["water"]:
        print("Not enough water")
        return False
    if beverage["ingredients"]["milk"] > Menu.resources["milk"]:
        print("Not enough milk")
        return False
    if beverage["ingredients"]["coffee"] > Menu.resources["coffee"]:
        print("Not enough coffee")
        return False
    else:
        return True


def make_beverage(beverage):
    Menu.resources["water"] -= beverage["water"]
    Menu.resources["milk"] -= beverage["milk"]
    Menu.resources["coffee"] -= beverage["coffee"]


while machine_is_running:
    choice = input("Espresso Cappuccino or Latte ?")
    choice = choice.lower()
    choice_customer = Menu.MENU[choice]
    if check_resources(choice_customer):
        penny_count = int(input("Pennies:"))
        nickel_count = int(input("Nickels:"))
        dime_count = int(input("Dimes:"))
        quarter_count = int(input("Quarters:"))
        coin_sum = check_coins(penny_count, nickel_count, dime_count, quarter_count)
        print(f"The total value is ${coin_sum}")
        if check_price(coin_sum, choice_customer["cost"]):
            balance += coin_sum
            make_beverage(choice_customer)
            return_change(coin_sum, choice_customer["cost"])
    if choice == "report":
        print_resources()
    if choice == "stop":
        machine_is_running = False

print(Menu.MENU["latte"])