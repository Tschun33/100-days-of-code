import random
from tkinter import *
from tkinter import messagebox

import pandas
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
timer = None
random_data = {}
card_to_learn = {}

# -------------Data Initialization-------------------------------

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


# -------------Flip Card---------------------------------------


def flip_card():
    global timer
    word = random_data["English"]
    canvas.itemconfig(word_card, text=word, fill="white")
    canvas.itemconfig(title_card, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=CARD_BACK)
    window.after_cancel(timer)


# -------------Card Right----------------------------------------


def card_right():
    global random_data
    data_dict.remove(random_data)
    df = pandas.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    generate_card()


# -------------Card Wrong----------------------------------------


def card_wrong():
    global random_data
    global card_to_learn
    generate_card()



# -------------Creating Cards------------------------------------


def generate_card():
    global random_data
    global timer
    try:
        random_data = random.choice(data_dict)
        word = random_data["French"]

    except IndexError:
        canvas.itemconfig(word_card, text="No Cards left")
        canvas.itemconfig(title_card, text="")
    else:
        canvas.itemconfig(word_card, text=word)
        canvas.itemconfig(title_card, text="French")
        timer = window.after(3000, flip_card)


# -------------IU Setup------------------------------------------


window = Tk()
window.title("FlashCard App")
window.config(padx=50, pady=80, bg=BACKGROUND_COLOR)

CARD_BACK = PhotoImage(file="images/card_back.png")
CARD_FRONT = PhotoImage(file="images/card_front.png")

BUTTON_RIGHT = PhotoImage(file="images/right.png")
BUTTON_WRONG = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=CARD_FRONT)
canvas.grid(column=0, row=0, columnspan=2)

title_card = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "italic"))

btn_wrong = Button(image=BUTTON_WRONG, command=card_wrong)
btn_wrong.grid(column=0, row=1)

btn_right = Button(image=BUTTON_RIGHT, command=card_right)
btn_right.grid(column=1, row=1)

generate_card()

window.mainloop()