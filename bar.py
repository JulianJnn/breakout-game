from turtle import Turtle


class Bar(Turtle):

    def __init__(self, xposition, yposition):
        super().__init__()
        self.penup()
        self.setposition(xposition, yposition)
        self.color("#8fd9a8")
        self.shape("square")
        self.shapesize(1, 5, 0)
        self.speed("fastest")
        self.bar_x = 0

    def go_right(self):
        self.bar_x += 20
        self.setx(self.bar_x)

    def go_left(self):
        self.bar_x -= 20
        self.setx(self.bar_x)
