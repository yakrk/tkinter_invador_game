from turtle import Turtle, Screen


class AlienAttack(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.x_move = 1
        self.y_move = -1
        self.move_speed = 2
        self.speed(self.move_speed)

    def set(self, position, img):
        self.goto(position)
        self.shape(img)
        self.penup()

    def move_down(self):
        # self.goto(position)
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def disappear(self):
        self.goto(50000,50000)