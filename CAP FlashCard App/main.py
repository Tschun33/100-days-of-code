import random
from tkinter import *
from tkinter import messagebox
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
# -------------Data Initialization-------------------------------

data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")

# -------------Creating Cards------------------------------------


def generate_card():
    random_data = random.choice(data_dict)
    word = random_data["French"]
    canvas.itemconfig(word_card, text=word)
    canvas.itemconfig(title_card, text="French")


# -------------IU Setup------------------------------------------
window = Tk()
window.title("FlashCard App")
window.config(padx=50, pady=80, bg=BACKGROUND_COLOR)

CARD_BACK = PhotoImage(file="images/card_back.png")
CARD_FRONT = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=CARD_FRONT)
canvas.grid(column=0, row=0, columnspan=2)

title_card = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "italic"))

BUTTON_RIGHT = PhotoImage(file="images/right.png")
BUTTON_WRONG = PhotoImage(file="images/wrong.png")

btn_wrong = Button(image=BUTTON_WRONG, command=generate_card)
btn_wrong.grid(column=0, row=1)

btn_right = Button(image=BUTTON_RIGHT, command=generate_card)
btn_right.grid(column=1, row=1)


window.mainloop()