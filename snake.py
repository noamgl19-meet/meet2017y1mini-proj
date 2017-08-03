import turtle
import random

turtle.tracer(1,0)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"
score = 1
        
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

SIZE_X = 800
SIZE_Y = 500

turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 1

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()




for num in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos += SQUARE_SIZE
    my_pos = (x_pos, y_pos)
    snake.goto(my_pos)
    pos_list.append(my_pos)
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)
    
def up():
    global direction
    direction = UP
#    move_snake()
    print("Up Key!")
def left():
    global direction
    direction = LEFT
#    move_snake()
    print("Left Key!")
def down():
    global direction
    direction = DOWN
#    move_snake()
    print("Down Key")
def right():    
    global direction
    direction = RIGHT
#    move_snake()
    print("Right Key")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()





food = turtle.clone()
food.shape("circle")
food.hideturtle()
food_stamps = []
food_pos = []
def make_food():
    min_x = -int(SIZE_X/2/SQUARE_SIZE)+1
    max_x = int(SIZE_X/2/SQUARE_SIZE)-1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y = int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
    pos_food = (food_x, food_y)
    
    food.goto(food_x,food_y)
    food_id = food.stamp()
    food_stamps.append(food_id)
    food_pos.append(pos_food)
    
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction == UP:
        snake.goto(x_pos, y_pos+ SQUARE_SIZE)
        print("You moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")

                         
    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    #########NEEED THIS FOR PART 5!
    global score
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        make_food()
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        stamp_list.append(snake.pos())
        turtle.clear()      
        turtle.write("score: " + str(score))
        score += 1
     
        


    
        
    #PART 8
        
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()
    turtle.ontimer(move_snake, TIME_STEP)
    if pos_list[-1] in pos_list[0: -1]:
        quit()


#food = turtle.clone()
#food.shape("circle")

#food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
#food_stamps = []
#food.hideturtle()

#for i in food_pos:
#    food.goto(i)
#    food_id = food.stamp()
#    food_stamps.append(food_id)

move_snake()
make_food()
score(0)
