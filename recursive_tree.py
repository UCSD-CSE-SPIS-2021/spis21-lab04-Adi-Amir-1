import turtle
turtle = turtle.Turtle()

def tree(trunkLength,height):

    if height > 0:

        turtle.forward(trunkLength)

        turtle.right(45)

        tree(trunkLength * .75,height - 1)

        turtle.left(90)

        tree(trunkLength * .75,height - 1)

        turtle.right(45)

        turtle.backward(trunkLength)
    


turtle.left(90)

turtle.up()

turtle.backward(100)

turtle.down()

turtle.color("black")

tree(200,5)

