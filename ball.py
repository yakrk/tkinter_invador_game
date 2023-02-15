from turtle import Turtle, Screen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 2
        self.speed(self.move_speed)

    def shoot(self):
        # self.goto(position)
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
    
    def set(self, position, ball_img):
        self.goto(position)
        self.shape(ball_img)
        self.penup()
    
    def disappear(self):
        self.goto(50000,50000)
        
        


    # def direction(self):
    #     if self.x_move > 0:
    #         is_moving_right = True
    #     else:
    #         is_moving_right = False
    #     return is_moving_right
