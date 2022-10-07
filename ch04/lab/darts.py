import pygame
import math
import random 

pygame.FULLSCREEN
pygame.init()
black= [0, 0, 0]
lightblue= [173, 216, 230]
pink= [255, 182, 193]

width=700
height=400
screen=pygame.display.set_mode([width, height])

#pygame.display.fill(blue)
pygame.draw.line(screen, black, ((width())/2,0), ((width)/2, height))
pygame.draw.line(screen, black, (0,(height)/2),(width, (height)/2)
pygame.draw.circle(screen, pink, (350,200), math.hypot(350, (200-0), 1)



pygame.display.flip()
pygame.window.exitonclick()