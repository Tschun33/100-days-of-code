import math
from tkinter import *
import pygame
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_work = ""
timer = None
# ---------------------------- SOUNDS ------------------------------- #
pygame.mixer.init()


def play_work():
    pygame.mixer.music.load("win31.mp3")
    pygame.mixer.music.play()


def play_break():
    pygame.mixer.music.load("wfw311.mp3")
    pygame.mixer.music.play()


# ---------------------------- TIMER RESET ------------------------------- #


def reset_app():
    global timer
    window.after_cancel(timer)
    global reps
    reps = 0
    timer = None
    global timer_text
    label_timer.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
    canvas.itemconfig(timer_text, text="00:00")
    label_check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global check_work
    reps += 1
    print(reps)
    if reps % 8 == 0:
        label_timer.config(text="Break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label_timer.config(text="Break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
    else:
        label_timer.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    clock = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=clock)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        if reps % 2 == 0:
            play_work()
        else:
            play_break()
        for _ in range(work_sessions):
            mark += "✔"
        label_check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

label_timer = Label()
label_timer.config(text="Timer", fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 40))
label_timer.grid(column=2, row=1)

label_check = Label()
label_check.config(text="", fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 10))
label_check.grid(column=2, row=3)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=1, row=3)

btn_reset = Button(text="Reset", command=reset_app)
btn_reset.grid(column=3, row=3)

window.mainloop()
