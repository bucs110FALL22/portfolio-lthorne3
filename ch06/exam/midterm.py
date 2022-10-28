import turtle
import random


t=turtle.Turtle()
window=turtle.Screen()
window.screensize(100,100)
cols= ["black", "white", "yellow"]
window.bgcolor(cols[0])


def draw_moon(radius, color):
  t.begin_fill()
  c=color
  t.color(c)
  r=radius
  t.circle(r)
  t.end_fill()
  

def draw_star(f):
  f
  t.color(cols[1])
  for i in range(0,5):
    t.forward(f)
    t.right(144)



def main():
  t.back(30)
  draw_moon(50, "yellow")
  t.forward(15)
  draw_moon(50,"black")
  for i in range(0,30):
    t.pu()
    t.right(random.randint(10, 350))
    t.forward(random.randint(30,60))
    t.pd()
    draw_star(random.randint(10,40))


main()
window.exitonclick()