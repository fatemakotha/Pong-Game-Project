from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with top and bottom:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with left and right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if r_paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect if l_paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()










































screen.exitonclick()