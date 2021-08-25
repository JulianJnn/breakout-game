from turtle import Screen
from bar import Bar
from ball import Ball
from scoreboard import Scoreboard
from blocks import Block

screen = Screen()
screen.setup(600, 800)
screen.bgcolor("#4b778d")
screen.title("Breakout")
screen.listen()
screen.tracer(0)

bar = Bar(0, -350)
ball = Ball()
scoreboard = Scoreboard()

default_x = [(75,150),(125,150),(175,150),(225,150),(275,150),(25,150), (-25,150), (-75,150),(-125,150),(-175,150),(-225,150),(-275,150),
             (75,180),(125,180),(175,180),(225,180),(275,180),(25,180), (-25,180), (-75,180),(-125,180),(-175,180),(-225,180),(-275,180),
             (75,210),(125,210),(175,210),(225,210),(275,210),(25,210), (-25,210), (-75,210),(-125,210),(-175,210),(-225,210),(-275,210),
             (75,240),(125,240),(175,240),(225,240),(275,240),(25,240), (-25,240), (-75,240),(-125,240),(-175,240),(-225,240),(-275,240),
             (75,270),(125,270),(175,270),(225,270),(275,270),(25,270), (-25,270), (-75,270),(-125,270),(-175,270),(-225,270),(-275,270),
             (75,300),(125,300),(175,300),(225,300),(275,300),(25,300), (-25,300), (-75,300),(-125,300),(-175,300),(-225,300),(-275,300)]
blocks_list = []

for x in default_x:
    block = Block(x)
    blocks_list.append(block)

screen.onkey(bar.go_left, "Left")
screen.onkey(bar.go_right, "Right")

block_count = 0

while block_count < 72:
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    for block in blocks_list :
        if block.distance(ball)< 25  :
            block.goto(1000,1000)
            block_count += 1
            ball.check_paddle()
            scoreboard.add_point_bar()


    if ball.xcor() >= 290 or ball.xcor() <= -290:
        ball.check_walls()

    if ball.ycor() >= 380:
        ball.check_paddle()

    if (ball.distance(bar) < 50 and ball.ycor() < -330) :
        ball.check_paddle()

    if ball.ycor() < -420:
        ball.goto(0, 0)
        ball.check_paddle()

screen.exitonclick()