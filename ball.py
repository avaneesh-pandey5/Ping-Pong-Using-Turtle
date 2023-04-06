from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize()
        self.pu()
    
    def move(self):
        self.goto(self.xcor()+5,self.ycor()+5)