import turtle

window=turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")
t.color("green")
#lines 7 & 8 needed to ask for user input but not needed when the function has parameters
#num_sides= int(input("How many sides? "))
#side_length= int(input("How long is each side? "))

def drawEqShape(num_sides, side_length):
  t
  num_sides
  side_length
  angle= 360/num_sides
  for i in [angle]*num_sides:
    t.forward(side_length)
    t.left(i)
  window.exitonclick()

drawEqShape(4, 25)