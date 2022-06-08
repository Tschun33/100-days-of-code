import random
print("Welcome to hangman")
word_list = ["cucumber"]
counter_wrong_guesses = 0
word = random.choice(word_list)
search = ["_"] * len(word)
guesses_char = set()


while counter_wrong_guesses < 5:
    char = input("Chose a letter:")
    if char in guesses_char:
        print("You already chose this letter")
        counter_wrong_guesses += 1
    else:

        i = 0
        guess_right = 0
        guesses_word = 0
        for x in word:
            if char == x:
                print("True")
                search[i] = x
                guess_right += 1
                guesses_word +=1
            else:
                print("False")
            i += 1
        if guess_right == 0:
            counter_wrong_guesses +=1
        if "_" not in search:
            print("You Won")
    guess_right = 0
    lives = 5 - counter_wrong_guesses
    guesses_char.add(char)
    print ("You have {} lives left".format(lives, 1))
    print(search)

print("You lose")