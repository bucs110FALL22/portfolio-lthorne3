import pygame
import math
import random 

#PART A
pygame.init()
black= [0, 0, 0]
lightblue= [173, 216, 230]
pink= [255, 182, 193]
width=700
height=400
window=pygame.display.set_mode([width, height])
window.fill(lightblue)

pygame.draw.line(window, black, (350,0), (350, 400))
pygame.draw.line(window, black, (0,200),(700, 200))
pygame.draw.circle(window, pink, [350, 200], 170, 0)
pygame.draw.rect(window, (0, 0, 255), [100, 100, 400, 100], 2)

#PART B
x= random.randrange(700)
y= random.randrange(400)
dartPos= (x,y)
pygame.draw.circle(window, black, [x,y], 2, 0)
distance_from_center = math.hypot(x-350, y-200) 
is_in_circle = distance_from_center <= width/2 


window.exitonclick



