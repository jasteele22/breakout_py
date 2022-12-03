from turtle import Turtle

class Ball(Turtle):

    def __init__(self,):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 1.5
        self.y_move = 1.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        if self.ycor() > 280:
            self.y_move += .2
            self.y_move *= -1
        if self.xcor() < -580:
            self.x_move += .2
            self.x_move *= -1
        if self.xcor() > 580:
            self.x_move += .2
            self.x_move *= -1

    def paddle_bounce(self):
        if self.ycor() > -265:
            self.y_move += .2
        self.x_move *= 1

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            # reverse the horizontal direction
            self.x_move *= -1

        if y_bounce:
            # reverse the vertical direction
            self.y_move *= -1

    def refresh(self):
        self.goto(0, -250)
        self.x_move *= -1
