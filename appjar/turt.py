# get the library
import turtle
import os

wind = turtle.Screen()
t = turtle.Turtle()

# draw a square
for loop in range(4):
    t.forward(100)
    t.right(90)

t.home()
yy = 10
for loop in range(100):
    t.dot ( yy,"cyan")
    yy=yy+5
t.home()
t.write("Finished - click window to close")
wind.exitonclick ( )