from turtle import Turtle

START = (0, -230)
MOVE = 10
FINISH = 480

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("DarkGreen")
        self.goto_start()
        self.setheading(90)

    def goto_start(self):
        self.goto(START)

    def move(self):
        self.forward(MOVE)

    def at_finish(self):
        if self.ycor() > 230:
            return True
        return False