from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.dx, self.dy = 1, 1

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

    def check_walls(self):
        self.dx *= -1

    def check_paddle(self):
        self.dy *= -1

