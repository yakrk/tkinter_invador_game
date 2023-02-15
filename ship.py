from turtle import Turtle, Screen


class Ship(Turtle):

    def __init__(self, position):
        super().__init__()
        img = r"C:\Users\yusuk\dev\projects\InvaderGame\images\pikachu.gif"
        screen = Screen()
        screen.addshape(img)
        self.shape(img)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
    
    def get_position(self):
        return (self.xcor(), self.ycor())