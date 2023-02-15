from score import Score
from ship import Ship
from alien import Alien
from ball import Ball
from alien_attack import AlienAttack
from turtle import Turtle, Screen
import random

# show screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic(
    r"images\grass_background.gif")
# screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# set images
ball_img = r"images\ball.gif"
screen.addshape(ball_img)
img1 = r"images\1.gif"
screen.addshape(img1)
img2 = r"images\2.gif"
screen.addshape(img2)
img3 = r"images\3.gif"
screen.addshape(img3)
img4 = r"images\4.gif"
screen.addshape(img4)
aliens_img = [img1, img2, img3, img4]
attack_img = r"images\attack.gif"
screen.addshape(attack_img)

# define class
ship = Ship((0, -250))
score = Score()
balls = []

# shoot ball


def shoot_ball():
    global balls
    global is_shot_alive
    is_shot_alive = True
    # if there are previous balls, move outside of screen
    if balls:
        balls[-1].goto(9000, 9000)
    balls.append(Ball())
    balls[-1].set((ship.xcor(), ship.ycor()), ball_img)


# define aliens
start_x_position = -280
start_y_position = 100
aliens = []
for j in range(4):
    y_position = j*40 + start_y_position
    for i in range(8):
        x_position = i * 70 + start_x_position
        aliens.append(Alien((x_position, y_position), aliens_img[j]))


# define initial variables
screen.listen()
screen.onkeypress(ship.go_left, "Left")
screen.onkeypress(ship.go_right, "Right")
screen.onkey(shoot_ball, "space")


# set ball action
game_is_on = True
is_shot_alive = False
is_alien_attack_alive = False

# function while game is on
while game_is_on:
    screen.update()
    # move aliens
    for alien in aliens:
        alien.move()
        if alien.xcor() > 280:
            alien.move_down()
            alien.bounce_x()
        elif alien.xcor() < -280:
            alien.move_down()
            alien.bounce_x()
        elif alien.ycor() < -250:
            game_is_on = False
            score.game_over()

    # aliens shoots
    if not is_alien_attack_alive:
        alien_to_attack = random.choice(aliens)
        alien_attack = AlienAttack()
        is_alien_attack_alive = True
        alien_attack.set(
            (alien_to_attack.xcor(), alien_to_attack.ycor()), attack_img)
    else:
        alien_attack.move_down()
        screen.update()
        if alien_attack.distance(ship) < 20:
            game_is_on = False
            score.game_over()
        if alien_attack.ycor() < -330:
            alien_attack.disappear()
            is_alien_attack_alive = False

    # disappear if shot hits
    if is_shot_alive:
        balls[-1].shoot()
        # is false if ball goes beyond ceiling
        if balls[-1].ycor() > 600:
            is_shot_alive = False
        # alien and ball disappear if hit
        for alien in aliens:
            if balls:
                if balls[-1].distance(alien) < 20:
                    alien.disappear()
                    aliens.remove(alien)
                    balls[-1].disappear()
                    score.add_score()


screen.exitonclick()
