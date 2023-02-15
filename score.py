from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-350, 250)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 14, "normal"))
    
    def add_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER! \n Your Score:{self.score}", align="center", font=("Arial", 30, "bold"))
