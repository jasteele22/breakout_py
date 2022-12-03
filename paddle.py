from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.setheading(0)
        self.setpos(x, y)

    def left(self,):
        self.bk(20)

    def right(self,):
        self.fd(20)
