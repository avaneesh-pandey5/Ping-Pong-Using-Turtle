from turtle import Turtle

HEIGHT = 5
WIDTH = 0.75
PADDLES = []

class Paddle(Turtle):

    def __init__(self,x_coordinate):

        super().__init__()
        self.new_paddle(x_coordinate)

    def new_paddle(self,x):
        
        self.goto(x,0)
        self.shape("square")
        self.color("white")
        self.pu()
        self.speed(0)
        self.shapetransform(0,WIDTH,HEIGHT,0)
        self.setheading(90)

        PADDLES.append(self)
    
    def up(self):

        self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        self.goto(self.xcor(),self.ycor()-20)