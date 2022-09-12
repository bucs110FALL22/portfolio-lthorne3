import turtle

sides= int(input("please enter num of sides:"))
length= int(input("please enter length of sides:"))
turt= turtle.Turtle()
turt.color("green")
turt.shape("turtle")
#turt.color("green") 
angle= 360/sides

for j in [angle]*sides:
  turt.forward(length)
  turt.left(angle)

window= turtle.Screen()
window.exitonclick()