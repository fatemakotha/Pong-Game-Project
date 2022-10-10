from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0)) #tuple
l_paddle = Paddle((-350, 0)) #tuple
# top_paddle = Paddle((200, 0)) #creates another paddle in the given location
ball = Ball()



screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()































screen.exitonclick()