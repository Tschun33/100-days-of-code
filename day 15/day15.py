import math

import Menu


def check_coins(penny, nickel, dime, quarter, price):
    sum_coins = round(penny * 0.01 + nickel * 0.05 + dime * 0.10 + quarter * 0.25, 2)
    return sum_coins


def print_resources():
    water = Menu.resources["water"]
    milk = Menu.resources["milk"]
    coffee = Menu.resources["coffee"]
    print(f"water: {water}, milk: {milk}, coffee: {coffee}")


def return_change(sum, price):
    change = sum - price
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


machine_is_running = True

while machine_is_running:
    choice = input("Espresso Capucchino or Latte ?")
    choice = choice.lower()
    choice_customer = Menu.MENU[choice]
    if check_resources(choice_customer):
        penny_count = int(input("Pennies:"))
        nickel_count = int(input("Nickels:"))
        dime_count = int(input("Dimes:"))
        quarter_count = int(input("Quarters:"))
        coin_sum = check_coins(penny_count, nickel_count, dime_count, quarter_count, choice_customer["cost"])
        print(f"The total value is ${coin_sum}")
    if choice == "stop":
        machine_is_running = False

print(Menu.MENU["latte"])