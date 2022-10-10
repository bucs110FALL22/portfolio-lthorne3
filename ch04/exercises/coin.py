import turtle
import random

franklin = turtle.Turtle()
window = turtle.Screen()
window.screensize(800,800)
franklin.shape("turtle")
franklin.color("purple")
on_screen= window.turtles() 
isInScreen= True



while isInScreen :
  coin = random.randrange(1, 3)
  if coin == 1:
    print('Heads')
    franklin.color("green")
    franklin.left(90)
    franklin.forward(50)
  if coin == 2:
    print ('Tails')
    franklin.color("yellow")
    franklin.right(90)
    franklin.forward(50)

  
  turtleX = franklin.xcor()
  turtleY = franklin.ycor()
  x_range = window.window_width()/2
  y_range = window.window_height()/2

    
  if abs(turtleX) > x_range or abs(turtleY) > y_range:
    isInScreen = False
    break

window.exitonclick()