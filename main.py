from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

pong_screen = Screen()
pong_screen.title("PONG BABY")

pong_screen.setup(800,600)
pong_screen.bgcolor("black")

pong_screen.tracer(0)

boundary = Turtle()
boundary.pu()
boundary.hideturtle()
boundary.goto(390,300)
boundary.color("White")
boundary.pd()
boundary.goto(390,-300)
boundary.goto(-400,-300)
boundary.goto(-400,300)
boundary.goto(390,300)


pong_screen.update()

pad1 = Paddle(380)
pad2 = Paddle(-390)

ball = Ball()

pong_screen.update()

score = Scoreboard()

pong_screen.listen()
pong_screen.onkeypress(pad1.up,"Up")
pong_screen.onkeypress(pad1.down,"Down")

pong_screen.onkeypress(pad2.up,"w")
pong_screen.onkeypress(pad2.down,"s")

game_is_on = True
ball.setheading(45)
num = 290

ball_is_at = "r"

while game_is_on:
    pong_screen.update()
    ball.fd(1.5)
    
    if ball.xcor() > 365 and ball.distance(pad1) < 60:
        ball.right(45)
        if ball_is_at == "r":
            score.Right_Score += 1
            ball_is_at = "l"
    
    if ball.xcor() < -370 and ball.distance(pad2) < 60:
        ball.right(45)
        if ball_is_at == "l":
            score.Left_Score += 1
            ball_is_at = "r"

    if ball.ycor() > 290:
        ball.right(45)

    if ball.xcor() > 410:
        # score.game_over()
        ball.goto(0,0)
    if ball.ycor() < -290:
        ball.right(45)
    if ball.xcor() < -420:
        # score.game_over()
        ball.goto(0,0)
    
    if ball.distance(pad1) < 15:
        ball.right(45)

    score.update_scoreboard()

pong_screen.exitonclick()