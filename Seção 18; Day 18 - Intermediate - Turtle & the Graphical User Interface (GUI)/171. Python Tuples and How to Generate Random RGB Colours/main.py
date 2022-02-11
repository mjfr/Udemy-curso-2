import turtle as t
import random

# Tuplas são estruturas de dados similares a listas, são ordenadas e não aceitam alterações a valores existentes
my_tuple = (1, 2, 3)
print(my_tuple[2])

# É possível converter tuplas em listas através do casting de list()
print(list(my_tuple))

tobby = t.Turtle()
# Decidimos que o colormode deve ir de 0 a 255
t.colormode(255)
tobby.shape("turtle")
tobby.width(12)
tobby.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color


directions = [0, 90, 180, 270]
for _ in range(200):
    tobby.color(random_color())
    tobby.forward(30)
    tobby.setheading(random.choice(directions))

