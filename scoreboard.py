from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.bar_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(0,0)
        self.write(self.bar_score,True,"center",("Courier", 80, "normal"))

    def add_point_bar(self):
        self.bar_score += 1
