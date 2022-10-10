from turtle import Turtle, Screen
import time
from paddle import Paddle
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle()
# paddle = Turtle("square")
# paddle.color("white")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(x=350, y=0)


# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(paddle.go_up, key="Up")
screen.onkey(paddle.go_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()































screen.exitonclick()