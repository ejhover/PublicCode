#Emmet Hoversten
#hover114
#CSCI 1133 Section 050
#Homework 1
import turtle
turtl = turtle.Turtle()
tri_side = int(input("How long should the triangle's side be? "))
turtl.showturtle()
#Draws three lines as long as the user requests and rotates to make a triangle
for i in range(3):
	turtl.fd(tri_side)
	turtl.right(120)
#Waits for the user to click the screen to stop running
turtle.exitonclick()
