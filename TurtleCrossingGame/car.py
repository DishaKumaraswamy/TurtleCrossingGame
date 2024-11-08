from turtle import Turtle
import random

colors = ["DarkMagenta" ,"Darkgoldenrod1" ,"gold1" , "salmon3", "steelblue3" ,"NavajoWhite3" ,"orchid3" ,"chocolate4", "burlywood4", "IndianRed4", "HotPink4", "DeepSkyBlue3", "Pink4", "Plum", "PaleVioletRed4", "turquoise", "purple4", "maroon4", "PaleGreen4", "cyan3", "black", "coral4", "DarkSlateBlue", "gray30", "gray60", "RosyBrown3", "RosyBrown4", "yellow3", "thistle3" ]
MOVE = 5

class Car:
    def __init__(self):
        self.cars = []
        self.speed = MOVE

    def create_cars(self):
        num = random.randint(1,6)
        if num == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.penup()
            yval = random.randint(-230, 230)
            new_car.goto(250, yval)
            self.cars.append(new_car)

    def move_cars(self):
        for i in self.cars:
            i.backward(self.speed)

    def level_up(self):
        self.speed += MOVE