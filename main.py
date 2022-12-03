from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick, Bricks
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=600, startx=-950, starty=0)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle(0, -275)
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=paddle.left, key="Left")
screen.onkey(fun=paddle.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.xcor() < -580 or ball.xcor() > 580:
        ball.wall_bounce()

    # detect collision with paddle
    pad_pos = paddle.position()
    if ball.ycor() < -255 and ball.distance(pad_pos) < 50:
        ball.paddle_bounce()

    #detect paddle misses ball
    if ball.ycor() < -280:
        # is_game_on = scoreboard.add_score_r()
        # if not is_game_on:
            # scoreboard.game_over()
            # game_is_on = False
        ball.clear()
        ball.y_move = 1.5
        ball.x_move = 1.5
        ball.refresh()

#     detect ball hit brick
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)
                scoreboard.add_score()

            # detect collision from left
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # detect collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


screen.exitonclick()
