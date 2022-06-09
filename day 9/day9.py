import os

is_playing = "yes"
d = {}
while is_playing == "yes":
    name = input("What is your name?")
    bid = input("What ist your offer?")
    d.update({name: bid})
    is_playing = input("Is there another person? 'yes' or 'no'")
    os.system('cls')

winner = max(d, key=d.get)
amount = d[winner]
print(f"The winner is: {winner} with ${amount}")
