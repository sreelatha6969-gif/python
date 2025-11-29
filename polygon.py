import turtle 
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
polygon.color("purple")
nu_sides=6
length = 60
angle = 360 / nu_sides
for i in range(nu_sides):
    polygon. forward(length)
    polygon.right(angle)
turtle.done() 