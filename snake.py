import time
import turtle
import random

#makes the turtle move smoothly
turtle.tracer(1,0)
SIZE_X = 800
SIZE_Y = 500
score1 = 1
#the screan size
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()
turtle.bgcolor("black")
score = turtle.clone()
score.ht()
SQUARE_SIZE = 20
START_LENTGH = 1

#lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
snake_colors = ["white", "red", "green", "grey" , "brown" , "yellow", "orange", "pink", "salmon","purple","olive","skyblue","greenyellow", "lightblue",]
scores = []
#set up position

snake = turtle.clone()
snake.shape("square")
snake.fillcolor("red")

#making the border
border = turtle.clone()

border.goto(400,-250)
border.pendown()
border.pen(fillcolor="white", pencolor="white", pensize=20)
border.pencolor("white")
border.goto(400,250)
border.goto(-400,250)
border.goto(-400, -250)
border.goto(400,-250)
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
food = turtle.clone()
food.fillcolor("white")
food.shape("circle")
food.hideturtle()

#locating the food
food_pos = []
food_stamps = []

#food.goto(food_pos[food_x, food_y])
#foodstamp = food.stamp()
#food_stamps.append(foodstamp)


#make food randomly
def make_food():
   
    min_x = -int(SIZE_X/2/SQUARE_SIZE)+1
    max_x = int(SIZE_X/2/SQUARE_SIZE)-1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y = int(SIZE_Y/2/SQUARE_SIZE)+1

    #PICK RANDOM PLACES
    food_x = random.randint(min_x, max_x)*SQUARE_SIZE
    food_y = random.randint(min_y, max_y)*SQUARE_SIZE
   
    food_tup = (food_x, food_y)
    food_pos.append(food_tup)
    food.goto(food_x, food_y)
    foodstamp = food.stamp()
    food_stamps.append(foodstamp)
    if food_x > 400:
        make_food()
    if food_x < -400:
        make_food()
    if food_y > 250:
        make_food()
    if food_y < -250:
        make_food()
    if food_tup in pos_list:
        food_stamps.pop(-1)
        food_pos.pop(-1)
        food_tup = food_stamps(-1)
        food.clearstamp(food_tup)
        make_food()
make_food()

    
#reset the game func
def reset():
    for i in range (len(stamp_list)):
        snake.clearstamp(stamp_list[i])
        stamp_list.pop(i)
#making the moving function
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved to the right!")
        snake.color(random.choice(snake_colors))
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved to the left!")
        snake.color(random.choice(snake_colors))
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved UP")
        snake.color(random.choice(snake_colors))
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved DOWN")
        snake.color(random.choice(snake_colors))
    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    
    old_stamp = stamp_list.pop(0)





    
    snake.clearstamp(old_stamp)
    #check if the snake is in the food position
    

    if snake.pos() in food_pos:
        global START_LENTGH, score1
        food_ind = food_pos.index(snake.pos()) #remove eaten food stamps
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!")
        stamp_list.append(snake1)
        pos_list.append(snake1)
        score1 += 1
        scores.append(score1)
        scores.sort()
        score.write("High Score: "+str(scores[-1]), move=False, align="left", font=("Arial", 18, "normal",))
        
        score.clear()
        score.pencolor("white")
        snake.pencolor("blue")
        score.write("Score: "+str(score1), move=False, align="left", font=("Arial", 18, "normal",))
        snake.fillcolor(random.choice(snake_colors))
        make_food()
    
    if snake.pos() in pos_list[0:-2]:
        
     
        quit()
        
        
    

    
    
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
    
