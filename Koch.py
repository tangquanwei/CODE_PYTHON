#KochV1
import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(800,800)
    turtle.pu()
    turtle.goto(-200,100)
    turtle.pd()
    turtle.pensize(1)
    level = 5
    length = 400
    koch(length,level)
    turtle.right(120)
    koch(length,level)
    turtle.right(120)
    koch(length,level)
    turtle.right(120)
    koch(length,level)
    turtle.hideturtle()
main()
#!
#?
#todo