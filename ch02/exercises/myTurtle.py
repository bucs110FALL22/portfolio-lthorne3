import turtle

my_turtle = turtle.Turtle()

num_sides = int(input("please enter the number of sides: "))
my_turtle.shape("turtle")
my_turtle.color("purple")
length= 50
angle= 360/ num_sides

for i in [angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.left(i)
  
  
my_turtle.up()
my_turtle.right(angle)
my_turtle.forward(20)
my_turtle.color("red")
my_turtle.down()
new_length= 20

for i in [angle]*num_sides:
  my_turtle.forward(new_length)
  my_turtle.left(i)


window = turtle.Screen()
window.exitonclick()




