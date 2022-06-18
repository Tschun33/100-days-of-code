import random
import data as ig_data
import os


def print_choice(choice):
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    print(f"{name}, {description}, {country}")


def determine_answer(person_a, person_b, guess):
    follower_a = person_a["follower_count"]
    follower_b = person_b["follower_count"]
    if follower_a >= follower_b and guess == "A":
        return True
    if follower_b >= follower_a and guess == "B":
        return True
    else:
        return False


is_playing = True
is_right = True
count_wins = 0


print("Welcome to my higher lower game")


while is_playing:
    choice_a = random.choice(ig_data.data)
    print_choice(choice_a)
    choice_b = random.choice(ig_data.data)
    print_choice(choice_b)
    player_guess = input("Who has more followers? Type 'A' or 'B':")
    det_answer = determine_answer(choice_a, choice_b, player_guess)
    if det_answer:
        os.system('cls')
        count_wins += 1
        print(f"Thats right! Your score is: {count_wins}")
    else:
        os.system('cls')
        is_playing = False
        print(f"Sorry, thats wrong. Your final score is: {count_wins} ")






