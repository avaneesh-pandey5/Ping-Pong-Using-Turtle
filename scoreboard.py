from turtle import Turtle
Right_Score = 0
Left_Score = 0

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.Right_Score = 0
        self.Left_Score = 0

        self.update_scoreboard()        

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.Left_Score} Score {self.Right_Score}",align="Center",font=("Courier", 30, "normal"))
    
    def game_over(self):
        if self.Right_Score>self.Left_Score:
            winner = "RIGHT WINS"
        elif self.Right_Score<self.Left_Score:
            winner = "LEFT WINS"
        else:
            winner = "  DRAW"

        self.goto(0,0)
        self.write(f"GAME OVER\n{winner}",align="Center",font=("Courier", 30, "normal"))
    

