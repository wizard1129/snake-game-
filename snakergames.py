import turtle
import time
import random
sc = turtle.Screen()
#screen
sc.bgcolor("cyan")
#sc.title("h")
#sc.setup(height=1000, width=1000)
#sc.tracer(0)
delay=0.1
segments = []
score = 0
high_score = 0

#snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0,100)
#snake.direction="stop"
direction = "stop"

#functions to move the snake
def move():
    global direction
    if direction=="up":
        y = snake.ycor()
        snake.sety(y+20)

    if direction=="down":
        y = snake.ycor()
        snake.sety(y-20)

    if direction=="left":
        x = snake.xcor()
        snake.setx(x-20)
    
    if direction=="right":
        x = snake.xcor()
        snake.setx(x+20)

#functions to link with the keys
def go_up():
    global direction
    direction="up"
def go_down():
    global direction
    direction="down"
def go_left():
    global direction
    direction="left"
def go_right():
    global direction
    direction="right"

sc.listen()
sc.onkey(go_up,"Up")
sc.onkey(go_down,"Down")
sc.onkey(go_right,"Right")
sc.onkey(go_left,"Left")

#food turtle
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,100)

#Pen turtle
pen = turtle.Turtle()
pen.penup()
pen.goto(0,150)
pen.hideturtle()
pen.write("Score:0 High Score:0", align="center", font=("Arial",30,   "normal"))

while True:
    sc.update()
    move()
    time.sleep(delay)
    if snake.distance(food)<20 :
        x = random.randint(-200,200)
        y= random.randint(-200,200)
        food.penup()
        food.goto(x,y)
        food.pendown()

    #increasing the length of snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
        score = score + 1

        if score>high_score:
            high_score = score
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Arial", 30, "normal"))


    for i in range(len(segments)-1,0,-1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x,y)

    if len(segments)>0:
            x = snake.xcor()
            y = snake.ycor()
            segments[0].goto(x,y)
