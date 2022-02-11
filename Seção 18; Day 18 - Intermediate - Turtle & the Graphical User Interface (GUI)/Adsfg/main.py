import turtle
from turtle import Turtle, Screen
from random import choice

# from colorgram import extract
#
# colors = extract('image.jpg', 500)
# only_rgb_list = []
#
#
# def get_colors():
#     for color_object in colors:
#         r = color_object.rgb.r
#         g = color_object.rgb.g
#         b = color_object.rgb.b
#         tuple_rgb = (r, g, b)
#         only_rgb_list.append(tuple_rgb)
#     return only_rgb_list
#
#
# print(get_colors())
turtle.colormode(255)
screen = Screen()
bob = Turtle("turtle")
bob.speed(10)
bob.penup()

color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63),
              (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
              (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217),
              (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178), (252, 197, 0),
              (29, 84, 92), (228, 174, 166), (186, 190, 201), (73, 73, 39)]

X_POS = -200
y_pos = -250
block_10x10 = 10
bob.setpos(X_POS, y_pos)
bob.hideturtle()
while block_10x10 != 0:
    for _ in range(10):
        bob.dot(20, choice(color_list))
        bob.forward(50)

    bob.setx(X_POS)
    y_pos += 50
    bob.sety(y_pos)
    block_10x10 -= 1

screen.exitonclick()
