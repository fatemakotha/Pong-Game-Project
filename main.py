from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0)) #tuple
l_paddle = Paddle((-350, 0)) #tuple
# top_paddle = Paddle((200, 0)) #creates another paddle in the given location
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()


    #Detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_horizontal()

    #Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    #Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()






























screen.exitonclick()