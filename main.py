import turtle
import time
import random

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("green")
screen.setup(width=700, height=500)

head = turtle.Turtle()
head.shape("triangle")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

food = turtle.Turtle() 
food.speed(0) 
food.shape("circle")
food.color("orange")
food.penup()
food.goto(random.randint(-300, 300), random.randint(-300, 300))

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")



segment= []


def add_segment():
  new_segment = turtle.Turtle()
  new_segment.speed(0)
  new_segment.shape("triangle")
  new_segment.color("blue")
  new_segment.penup()
  segment.append(new_segment)

while True:

  screen.update()

  if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor:
    time.sleep(1)
  head.goto(0,0)
  head.direction = "Stop"
  
  
  for segment in segment:
    segment.goto(1000,1000)
    
  segment.clear()
  head.write("You lose", align = "center", font = ("Zalgo", 24, "bold"))


  if head.distance(food) < 20:
    food.goto(random.randint(-300, 300), random.randint(-300, 300))
    add_segment()

  for index in range(len(segment)-1, 0, -1):
    x = segment[index-1].xcor()
    y = segment[index-1].ycor()
    segment[index].goto(x,y)

  if len(segment) > 0:
    x = head.xcor()
    y = head.ycor()
    segment[0].goto(x,y)


  move()
  time.sleep(0.1)



                   
