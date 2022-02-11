from turtle import Turtle, Screen

franklin = Turtle("turtle")
franklin_colors = ["dark slate blue", "red", "lime green", "black", "orange", "pink", "yellow", "purple"]
shape_vertices = 3

while shape_vertices != 11:
    franklin.color(franklin_colors[shape_vertices-3])
    for _ in range(shape_vertices):
        franklin.forward(100)
        franklin.right(360/shape_vertices)
    shape_vertices += 1


screen = Screen()
screen.exitonclick()
