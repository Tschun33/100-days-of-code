import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)
    if reps % 8 == 0:
        label_timer.config(text="Break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(LONG_BREAK_MIN*5)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*5)
        label_timer.config(text="Break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
    else:
        label_timer.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(WORK_MIN*5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    clock = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=clock)
    if count > 0:
        window.after(1000, count_down, count - 1)
    if count == 0 and reps < 8:
        start_timer()

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
label_check.config(text="✔", fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 10))
label_check.grid(column=2, row=3)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=1, row=3)

btn_reset = Button(text="Reset")
btn_reset.grid(column=3, row=3)

window.mainloop()

