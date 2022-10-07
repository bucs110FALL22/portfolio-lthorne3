import pygame
import math
import random

#PART A
pygame.init()
black = [0, 0, 0]
lightblue = [173, 216, 230]
pink = [255, 182, 193]
green = [0, 255, 0]
red = [255, 0, 0]
blue = [0, 0, 255]
width = 400
height = 400
window = pygame.display.set_mode([width, height])

window.fill(lightblue)
pygame.draw.circle(window, pink, [200, 200], 170, 0)
pygame.draw.line(window, black, (200, 0), (200, 400))
pygame.draw.line(window, black, (0, 200), (400, 200))

#PART C
r = pygame.Rect(15, 300, 75, 75)
b = pygame.Rect(285, 300, 75, 75)
pygame.draw.rect(window, blue, r)
pygame.draw.rect(window, red, b)

choice = int(input("Do you think player 1 or player 2 will win? "))
if choice == 1:
    print("You chose player 1")
if choice == 2:
    print("You chose player 2")

#PART B
x = random.randrange(400)
y = random.randrange(400)
dartPos = (x, y)
distance_from_center = math.hypot(x - 200, y - 200)
is_in_circle = distance_from_center <= width / 2
p1_points = 0
p2_points = 0
for i in range(11):
    pygame.draw.circle(window, blue, [x, y], 5, 0)
    if is_in_circle:
        p1_points = p1_points + 1
    pygame.draw.circle(window, red, [x, y], 5, 0)
    if is_in_circle:
        p2_points = p2_points + 1

pygame.time.wait(500)
pygame.display.flip()
pygame.time.wait(10000)

print(p1_points)
print(p2_points)
if p1_points > p2_points and choice == 1:
    print("You were right! Player 1 wins.")
if p1_points > p2_points and choice == 2:
    print("You were wrong. Player 2 wins.")
if p1_points < p2_points and choice == 2:
    print("You were right! Player 2 wins.")
if p1_points > p2_points and choice == 2:
    print("You were wrong. Player 1 wins.")
if p1_points == p2_points:
    "It was a tie."
