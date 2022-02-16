import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
scoreboard = Scoreboard()
cars = []

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
new_car_timer = 0
stage = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generates a car every 6th time the game loops
    if new_car_timer == 6:
        new_car_timer = 0
        car = CarManager((300, randint(-250, 250)))
        car.speed_increase(scoreboard.stage)  # The speed changes according to the current stage
        cars.append(car)
    new_car_timer += 1

    # Moves every car generated
    for car in cars:
        car.move()

    # Detecting top screen collision
    if player.ycor() > 280:
        player.next_level()
        scoreboard.level_up()
        scoreboard.refresh_scoreboard()

        # Clears the cars from the screen and from its list
        for car in cars:
            car.car_clear()
        cars = []

    # Detecting car collision
    for car in cars:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
