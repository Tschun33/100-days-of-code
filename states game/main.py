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
print(all_states)


guessed_states = []

# for state in data:
#     new_state = State(name=data["state"], x=data["x"], y=data["y"])
#     print(data["state"])
#     states.append(new_state)

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title="Guess a State", prompt="What is another States name?")
    print(answer_state)

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()