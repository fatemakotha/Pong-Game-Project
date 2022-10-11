from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")


paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.goto(x=350, y=0)

def go_up():
    new_y = paddle.ycor() + 10
    paddle.goto(x=350, y=new_y)

def go_down():
    new_y = paddle.ycor() - 10
    paddle.goto(x=350, y=new_y)


screen.listen()
screen.onkey(go_up, key="Up")
screen.onkey(go_down, key="Down")





































screen.exitonclick()