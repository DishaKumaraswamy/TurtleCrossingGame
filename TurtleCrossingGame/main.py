from turtle import Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard
import time


sc = Screen()
sc.setup(width=500, height=500)
sc.bgcolor("CornSilk")
sc.title("Turtle Crossing")
sc.tracer(0)


tim = Player()
car = Car()
score = ScoreBoard()

sc.listen()
sc.onkey(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sc.update()
    car.create_cars()
    car.move_cars()

    for i in car.cars:
        if i.distance(tim) < 30:
            game_is_on = False
            score.game_over()

    if tim.at_finish():
        tim.goto_start()
        car.level_up()
        score.level_increase()

sc.exitonclick()