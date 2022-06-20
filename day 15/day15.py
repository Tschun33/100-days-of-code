import math

import Menu


def check_coins(penny, nickel, dime, quarter):
    sum_coins = round(penny * 0.01 + nickel * 0.05 + dime * 0.10 + quarter * 0.25, 2)
    return sum_coins


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
    penny_count = int(input("Pennies:"))
    nickel_count = int(input("Nickels:"))
    dime_count = int(input("Dimes:"))
    quarter_count = int(input("Quarters:"))
    coin_sum = check_coins(penny_count, nickel_count, dime_count, quarter_count)
    print(f"The total value is ${coin_sum}")
    machine_is_running = False

