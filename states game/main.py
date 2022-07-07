import turtle
import pandas as pd
from state import State

screen = turtle.Screen()
screen.setup(height=491, width=725)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guesses = 0
states = []

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()


guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",
                                    prompt="What is another States name?").title()
    print(answer_state)

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    if answer_state == "Exit":
        break

states_to_learn = list(set(all_states) - set(guessed_states))
new_data = pd.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
print(states_to_learn)




