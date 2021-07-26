import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# to get coordinates of state on the image

# def get_mouse_click_coord(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coord)

# turtle.mainloop() # screen doesnt close when click
data = pandas.read_csv("50_states.csv")
num_of_states = 0


while num_of_states < 50:
    answer_state = screen.textinput(title=f"{num_of_states}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == 'Exit':
        break
    if len(data[data.state == answer_state]) > 0:
        data_point_x = data[data.state == answer_state].values.tolist()[0][1]
        data_point_y = data[data.state == answer_state].values.tolist()[0][2]
        num_of_states += 1
        state = turtle.Turtle()
        state.penup()
        state.speed("fastest")
        state.hideturtle()
        state.goto(data_point_x, data_point_y)
        state.write(f"{answer_state}", align="center", font=("Arial", 8, "normal"))
        data = data.drop([data[data.state == answer_state].index[0]])

data.to_csv("states_to_learn.csv")
