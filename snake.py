import turtle
import random
#makes the turtle move smoothly
turtle.tracer(1,0)
SIZE_X = 800
SIZE_Y = 500
#the screan size
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()

SQUARE_SIZE = 20
START_LENTGH = 7

#lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#set up position
snake = turtle.clone()
snake.shape("square")

#hide the turtle
turtle.hideturtle()

for i in range(START_LENTGH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    x_pos += SQUARE_SIZE
    my_pos = (x_pos, y_pos)
    snake.goto(x_pos, y_pos)
    pos_list.append(my_pos)
    snake1 = snake.stamp()
    stamp_list.append(snake1)
#defining the arrow keys
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100 #update snake position
SPACEBAR = "space"
#starting turn

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP
#border
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
#arrow functions
def up():
    global direction #makes the direction variuble usable in this function
    direction = UP # turns up
    
    print("you pressed the UP ARROW key")
def left():
    global direction #makes direction usable in this function
    direction = LEFT #turns left
    print("you pressed the LEFT ARROW key!")
def down():
    global direction # makes direction usable in this function
    direction = DOWN #turns down
    print("you pressed the DOWN ARROW key")
def right():
    global direction #makes direction usable in this function
    direction = RIGHT #turns right
    print("you pressed the RIGHT ARROW key")
#using the functions
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

#making the moving function
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved to the right!")
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved to the left!")
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved UP")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved DOWN")
    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    #check if the snake is in the food position
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos()) #remove eaten food stamps
        food_pos.pop(food_ind)
        print("you have eaten the food!")
    pos_list.pop(0)


    #Grab position of the snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    #check if the snake touch the border
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the border! GAME OVER!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you hit the border! GAME OVER!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("you hit the border! GAME OVER!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("you hit the border! GAME OVER!")
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
    #TODO add trash
#turtle.register_shape("circle")
food = turtle.clone()
food.shape("turtle")
food.hideturtle()

#locating the food
food_pos = [(100,100), (-100,100) , (-100, -100) , (100, -100)]
food_stamps = []
food.goto(food_pos[0])
foodstamp = food.stamp()
food_stamps.append(foodstamp)
food.goto(food_pos[1])
foodstamp = food.stamp()
food_stamps.append(foodstamp)
food.goto(food_pos[2])
foodstamp = food.stamp()
food_stamps.append(foodstamp)
food.goto(food_pos[3])
foodstamp = food.stamp()
food_stamps.append(foodstamp)

    
    

