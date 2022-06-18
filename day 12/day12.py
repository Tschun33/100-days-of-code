from random import randint


EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def check_answer(guess, answer, guesses):
    if guess > answer:
        print("Number is too high")
        return guesses - 1
    elif guess < answer:
        print("Number is too low")
        return guesses - 1
    else:
        print(f"You got it! The number was {answer}")


def game():
    print("Welcome to the number guessing game!")
    print("Im thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst number is {answer}")
    guesses = set_difficulty()
    guess = 0
    while guess != answer and guesses > 0:
        print(f"You have {guesses} guesses remaining.")
        guess = int(input("Make a guess:"))
        guesses = check_answer(guess, answer, guesses)
    if guesses == 0:
        print("You Lost")


game()