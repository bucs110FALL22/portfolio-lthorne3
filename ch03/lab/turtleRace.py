import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

## 5. Your PART A code goes here
for i in range(10):
  michelangelo.forward(random.randrange(0,11))
  turtle.time.wait(500)
  leonardo.forward(random.randrange(0,11))
  turtle.time.wait(500)

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode([1000,2000])

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)




for i in range(5):
  num_sides= int(input("How many sides: "))
  side_length= int(input("How long is each side: " ))
  offset= int(input("How far from top corner: "))
  shape_color= color(input("What color)"))
  coords=[]
  for j in range(side_length):
    theta = (2.0 * math.pi * i) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.add([x,y])
  shape= pygame.draw.polygon(window, shape_color, [coords])
  print(shape)
  pygame.display.flip()
  pygame.time.wait(500)
  window.fill


pygame.window.exitonclick()