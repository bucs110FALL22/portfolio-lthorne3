import turtle
import random

franklin = turtle.Turtle()
window = turtle.Screen()
window.screensize(400,400)
franklin.shape("turtle")
franklin.color("purple")
on_screen= window.turtles() 

def isInScreen(window, franklin):
    if random.random() > 0.1:
        return True
    else:
        return False

while isInScreen(window, franklin):
  coin = random.randint(1, 2)
  if coin == 1:
    print('Heads')
    turtle.left(90)
  if coin == 2:
    print ('Tails')
    turtle.right(90)
  turtle.forward(50)


window.exitonclick()