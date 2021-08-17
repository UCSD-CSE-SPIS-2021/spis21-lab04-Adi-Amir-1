import turtle
turtle = turtle.Turtle()

def snowflake(side_length, levels):
  snowflake_side(side_length, levels)
  turtle.right(120)
  snowflake_side(side_length, levels)
  turtle.right(120)
  snowflake_side(side_length, levels)

def snowflake_side(side_length, levels):
    if(levels == 0):
        turtle.forward(side_length)
    else:
        
        snowflake_side(side_length, levels-1)
        turtle.left(60)
        snowflake_side(side_length, levels-1)
        turtle.right(120)
        snowflake_side(side_length, levels-1)
        turtle.left(60)
        snowflake_side(side_length, levels-1)

snowflake(50, 5)