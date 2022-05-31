import random

player_choice = int(input("Chose 0 for rock, 1 for paper or 2 for scissor:\n"))
rps = ["rock", "paper", "scissor"]
computer_choice = random.randint(0, 2)
if 0 < player_choice < 3:
    print("Your choice was: " + rps[player_choice])
print("Computer choice was: " + rps[computer_choice])
if player_choice == computer_choice:
    print("It\'s a draw!")
elif player_choice < 0 or player_choice > 2:
    print("You typed an invalid number, you Lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You Win!")
elif player_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif player_choice > computer_choice:
    print("You Win!")


