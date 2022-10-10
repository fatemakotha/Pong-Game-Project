from turtle import Turtle, Screen
import time
class Paddle(Turtle):
    def __init__(self, position): #position is a tuple
        super().__init__()
        self.shape("square")
        self.color("white")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position) #position is a tuple, i.e. (-350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


