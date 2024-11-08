from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("MidnightBlue")
        self.level = 1
        self.goto(-230, 210)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level : {self.level}" ,align= "left", font=("Helvetica", 12, "normal"))

    def level_increase(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.color("firebrick4")
        self.write(" GAME OVER " ,align= "center", font=("Helvetica", 12, "normal"))
