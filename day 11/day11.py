import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_playing = True
next_card = True
dealer_next_card = True

dealer = []
player = []


player.append(random.choice(cards))
player.append(random.choice(cards))
dealer.append(random.choice(cards))
print(f"Player's Hand: {player}")
print(f"Dealer's Hand: {dealer}")

if sum(player) == 21:
    print("You Won")
    is_playing = False
    next_card = False
    dealer_next_card = False

while next_card:
    choice = input("Do you want one more card? 'yes' or 'no' ")
    if choice == "yes":
        player.append(random.choice(cards))
        print(f"Player's Hand: {player}")
        if sum(player) > 21:
            print("Your Lose")
            dealer_next_card = False
            next_card = False
            is_playing = False
        if sum(player) == 21:
            print("You Won")
            is_playing = False
            next_card = False
            dealer_next_card = False
    elif choice == "no":
        if sum(player) < 17:
            print("You have to pick a card")
        else:
            next_card = False
    else:
        print("No valid input")

while dealer_next_card:
    dealer.append(random.choice(cards))
    dealer_next_card = False
    print(f"Dealer Hand: {dealer}")
    if sum(dealer) > 21:
        print("You Win")
        dealer_next_card = False
    elif sum(dealer) < sum(player) and sum(dealer) < 17:
        dealer_next_card = True
    elif sum(dealer) == sum(player):
        print("Draw")
        print(f"Player Hand: {player}")
        print(f"Dealer Hand: {dealer}")
        dealer_next_card = False
    elif sum(dealer) < sum(player):
        dealer_next_card = True
    elif sum(dealer) > sum(player):
        print("You Lose")
        print(f"Player Hand: {player}")
        print(f"Dealer Hand: {dealer}")
        dealer_next_card = False

