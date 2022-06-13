from random import randint

print("Welcome to the number guessing game!")
print("Im thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
guesses = 0

number = randint(1, 100)


if difficulty == "easy":
    guesses = 10
elif difficulty == "hard":
    guesses = 5
else:
    print("No valid input")


while guesses > 0:
    print(f"You have {guesses} guesses remaining.")
    guess = int(input("Make a guess:"))
    if guess > number:
        print("Number is too high")
        guesses -= 1
    elif guess < number:
        print("Number is too low")
        guesses -= 1
    elif guess == number:
        guesses = 0
        win = True

if win:
    print("You won!")
else:
    print("You lost!")

print(f"My number was {number}")





