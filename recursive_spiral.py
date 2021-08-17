import turtle
turtle = turtle.Turtle()

def spiral(initial_length, angle, multiplier):
    if initial_length < 300:
        turtle.forward(initial_length)
        turtle.left(angle)
        spiral(initial_length*multiplier, angle, multiplier)

spiral(10, -45, 1.1)
       