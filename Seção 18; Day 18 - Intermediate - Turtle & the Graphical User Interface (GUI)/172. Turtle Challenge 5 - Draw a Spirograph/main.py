import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
tobias = Turtle("turtle")
tobias.speed(0)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple


# next_circle_angle = 6
# next_line_angle = 12
# # Quantidade de círculos --> 360 / Ângulo de virada
# for _ in range(int(360 / next_circle_angle)):
#     # Qtd. de linhas que formam o círculo --> (360/ângulo de virada da próxima linha reta) = Qtd. de linhas do círculo
#     for _ in range(int(360 / next_line_angle)):
#         # Tamanho de cada linha que forma o círculo
#         tobias.forward(40)
#         # Ângulo de virada da próxima linha reta
#         tobias.right(next_line_angle)
#     tobias.color(random_color())
#     # Ângulo de virada para o próximo círculo
#     tobias.right(next_circle_angle)

# Utilizando o próprio método de círculo da turtle --> Muito mais rápido que o meu
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tobias.color(random_color())
        tobias.circle(100)
        current_heading = tobias.heading()
        tobias.setheading(current_heading + 10)


draw_spirograph(4)

# Comentado, mas é incrível! Isso faz uma rosquinha!!!!!!!!!!
# while True:
#     for _ in range(20):
#         tobias.forward(30)
#         tobias.right(15)
#     tobias.forward(50)
#     tobias.right(10)
#     if abs(tobias.pos()) < 1:
#         break

screen.exitonclick()
