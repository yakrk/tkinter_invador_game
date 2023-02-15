from turtle import Turtle, Screen

class Alien(Turtle):
    def __init__(self, position, img):
        super().__init__()
        self.shape(img)
        self.penup()
        self.goto(position)
        self.x_move = 1
        self.y_move = -10
        self.move_speed = 2
        self.speed(self.move_speed)

    def disappear(self):
        self.goto(50000,50000)

    def move_down(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def bounce_x(self):
        self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())
