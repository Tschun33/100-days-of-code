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

while next_card:
    choice = input("Do you want one more card? 'yes' or 'no' ")
    if choice == "yes":
        player.append(random.choice(cards))
        print(f"Player's Hand: {player}")
        if sum(player) > 21:
            print("Your Lose")
            next_card = False
            is_playing = False
    elif choice == "no":
        next_card = False
    else:
        print("No valid input")

while dealer_next_card:
    dealer.append(random.choice(cards))
    if sum(dealer)