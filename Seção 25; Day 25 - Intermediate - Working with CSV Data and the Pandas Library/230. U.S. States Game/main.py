import turtle
from turtle import Screen, Turtle
import pandas
from state_manager import State

screen = Screen()
screen.title("U.S. State Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
screen.setup(width=725, height=491)
turtle.shape(IMAGE)

# Obtendo valores das coordenadas a partir do click do mouse
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinate)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
states_x_cor = states_data.x.to_list()
states_y_cor = states_data.y.to_list()
STATES_COUNT = len(states_list)

answer_state = screen.textinput(title="Guess the State", prompt="Type a U.S. State name").title()
guessed_states = []
# turtle.mainloop()
while len(guessed_states) < 50:
    # screen.update()
    if answer_state == "Exit":
        break
    elif len(states_list) == 1:
        state.win()
        break
    elif answer_state in states_list:
        correct_state_index = states_list.index(answer_state)
        state = State((states_x_cor[correct_state_index], states_y_cor[correct_state_index]), answer_state)
        states_x_cor.pop(correct_state_index)
        states_y_cor.pop(correct_state_index)
        guessed_states.append(states_list.pop(correct_state_index))
        answer_state = screen.textinput(title=f"Score: {(STATES_COUNT-len(states_list))} / {STATES_COUNT}",
                                        prompt="What's another state's name?").title()
    else:
        if guessed_states.count(answer_state):
            answer_state = screen.textinput(title=f"Score: {(STATES_COUNT-len(states_list))} / {STATES_COUNT}",
                                            prompt=f"You already guessed {answer_state}"
                                                   f"\nWhat's another state's name?").title()
        else:
            answer_state = screen.textinput(title=f"Score: {(STATES_COUNT-len(states_list))} / {STATES_COUNT}",
                                            prompt=f"There's no {answer_state} state"
                                                   f"\nWhat's another state's name?").title()

states_not_guessed = {
    "States": states_list
}
sng_dataframe = pandas.DataFrame(states_not_guessed)
sng_dataframe.to_csv("states_to_learn.csv")
# Alternativa para o screen.exitonclick()
# screen.exitonclick()
