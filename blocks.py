from turtle import Turtle

class Block(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.color("#8fd9a8")
        self.penup()
        self.shape("square")
        self.shapesize(1, 2,0)
        self.goto(pos)