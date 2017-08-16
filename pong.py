import turtle
import time
import random


# randomizing the ball's Y scale
pong_y = (random.random()) * 350
# setting screan size
SIZE_X = 1280
SIZE_Y = 760
turtle.setup(SIZE_X, SIZE_Y)

# the speed/grid
SQUARE_SIZE = 20

# refresh every 100 miliseconds
TIME_STEP = 100

TIME_STEP_BALL = 10

# cloning turtles
player1 = turtle.clone()

player2 = turtle.clone()
ball = turtle.clone()

ball.ht()
ball.penup()
ball.fillcolor("red")
ball.shape("circle")
turtle.ht()

# setting starting players position
player1.penup()
player1.shape("square")
player1.turtlesize(4)

player1.ht()
player1.goto(SIZE_X / 2 - SQUARE_SIZE - 2, 0)
player1.st()
player2.penup()
player2.shape("square")
player2.turtlesize(4)

player2.ht()
player2.goto(-SIZE_X / 2 + SQUARE_SIZE + 2, 0)
player2.st()
ball.goto(- SIZE_X / 2 + SQUARE_SIZE, 0)
ball.st()
# defining ARROW keys
UP_ARROW = "Up"
DOWN_ARROW = "Down"

# giving values

UP = 0
DOWN = 1
# starting p1's direction == up
p1direction = UP
# starting p2's direction == down
p2direction = DOWN


# up function
def p1up():
    global p1direction
    p1direction = UP


# down functionw
def p1down():
    global p1direction
    p1direction = DOWN


# p2 up function
def p2up():
    global p2direction
    p2direction = UP


# p2 down function
def p2down():
    global p2direction
    p2direction = DOWN


# detecting key press of p1
turtle.onkeypress(p1up, "Up")
turtle.onkeypress(p1down, "Down")
# detecting keypress of p2
turtle.onkeypress(p2up, "w")
turtle.onkeypress(p2down, "s")

turtle.listen()


# making the moovment of p1
def move_p1():
    global SQUARE_SIZE, TIME_STEP, p2_x, p2_y
    # defining p1's x and y
    player1_pos = player1.pos()
    p1_x = player1_pos[0]
    p1_y = player1_pos[1]
    if p1direction == UP:
        player1.goto(p1_x, p1_y + SQUARE_SIZE)
    if p1direction == DOWN:
        player1.goto(p1_x, p1_y - SQUARE_SIZE)

    turtle.ontimer(move_p1, TIME_STEP)


# p2 function
def move_p2():
    global SQUARE_SIZE, TIME_STEP, p1_x, p1_y, player1_pos
    # defining p2's x and y
    player2_pos = player2.pos()
    p2_x = player2_pos[0]
    p2_y = player2_pos[1]

    # choosing which position to go
    if p2direction == UP:
        player2.goto(p2_x, p2_y + SQUARE_SIZE)
    if p2direction == DOWN:
        player2.goto(p2_x, p2_y - SQUARE_SIZE)

    turtle.ontimer(move_p2, TIME_STEP)


def move_ball():
    global pong_y
    ball_pos = ball.pos()
    ball_x = ball_pos[0]
    ball_y = ball_pos[1]
    if ball_pos[0] < -SIZE_X / 2:
        print("hey")


    if -80 < player2.pos()[0] - ball.pos()[0] < 80 and -80 < player2.pos()[1] - ball.pos()[1] < 80:
        print("suc")
        ball.goto(ball_x + SIZE_X, pong_y)
    pong_y = (random.random()) * 350


def move_ball2():
    global pong_y
    ball_pos = ball.pos()
    ball_x = ball_pos[0]
    ball_y = ball_pos[1]
    if ball_pos[0] < -SIZE_X / 2:
        print("hey")

    if -80 < ball.pos()[0] - player1.pos()[0] < 80 and -80 < ball.pos()[1] - player1.pos()[1] < 80:
        ball.goto(ball_x - SIZE_X, pong_y)
    pong_y = (random.random()) * 350


move_p2()
move_p1()

move_ball()
move_ball2()
if move_ball():
    pong_y = (random.random()) * 350

    move_ball2()
if move_ball2():
    pong_y = (random.random()) * 350

    move_ball()
ball_pos = ball.pos()

if ball_pos[0] > SIZE_X/2:
    turtle.goto(0,0)
    turtle.write("player2 won!", font=("Ariel", 22, "normal"))
    time.sleep(5)
    quit()
elif ball_pos[0] < -SIZE_X/2:
    turtle.goto(0,0)
    turtle.write("player1 won!", font=("Ariel", 22, "normal"))
    time.sleep(5)
    quit()
turtle.mainloop()
