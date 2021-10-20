import turtle as t


def male(x, y):
    t.penup()
    t.goto(x, y)
    t.pensize(10)
    t.pendown()
    # head
    t.fillcolor("blue")  # 1.0,0,0.5
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    x = t.xcor()
    y = t.ycor()
    # right eye
    t.pensize(15)
    t.penup()
    t.goto(x+20, y+70)
    t.pendown()
    t.fd(-1)
    # left eye
    t.penup()
    t.goto(x-20, y+70)
    t.pendown()
    t.fd(1)
    # mouth
    t.penup()
    t.pensize(5)
    t.goto(x-10, y+30)
    t.pendown()
    t.right(90)
    t.circle(10, 180)
    # reset
    t.penup()
    t.goto(x, y)
    t.pensize(10)
    t.pendown()
    # up body
    t.right(180)
    t.forward(60)
    x = t.xcor()
    y = t.ycor()
    # hand1
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(40)
    # hand2
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.right(180)
    t.forward(30)  # y-=30
    t.left(90)
    t.forward(70)
    t.right(90)
    t.forward(40)
    # down body
    t.penup()
    t.goto(x, y-30)
    t.pendown()
    t.forward(100)  # y-=130
    # leg front
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(60)
    # leg behind
    t.penup()
    t.goto(x, y-130)
    t.pendown()
    t.right(45)
    t.forward(60*1.4)

    # reset
    t.left(135)


def female(x, y):
    t.penup()
    t.goto(x, y)
    t.pensize(10)
    t.pendown()
    # head
    t.fillcolor("pink")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    x = t.xcor()
    y = t.ycor()
    # right eye
    t.pensize(15)
    t.penup()
    t.goto(x+20, y+70)
    t.pendown()
    t.fd(-1)
    # left eye
    t.penup()
    t.goto(x-20, y+70)
    t.pendown()
    t.fd(1)
    # mouth
    t.penup()
    t.pensize(5)
    t.goto(x-10, y+30)
    t.pendown()
    t.right(90)
    t.circle(10, 180)
    # reset
    t.penup()
    t.goto(x, y)
    t.pensize(10)
    t.pendown()
    # up body
    t.right(180)
    t.forward(60)
    x = t.xcor()
    y = t.ycor()
    # hand1
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(40)
    # body
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.right(135)
    t.forward(30)  # y-=30
    # hand2
    t.right(45)
    t.forward(50)
    t.right(90)
    t.forward(40)
    # down body
    t.penup()
    t.goto(x, y-30)
    t.pendown()
    t.left(135)
    t.forward(100)  # y-=130
    # leg front
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(60)
    # leg behind
    t.penup()
    t.goto(x, y-130)
    t.pendown()
    t.right(45)
    t.forward(60*1.4)
    # reset
    t.left(135)


def heart(x, y):
    t.penup()
    t.goto(x, y)
    t.pensize(4)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    t.left(40)
    t.forward(100)
    t.circle(50, 210)
    t.right(135)
    t.circle(50, 210)
    t.forward(100)
    t.end_fill()
    t.hideturtle()

def biu(x,y):
    t.penup()
    t.goto(x, y)
    t.pensize(4)
    t.pendown()
    t.pencolor("red")
    t.write("Biu~", align="center",font=("Arial", 18, "normal"))

# if __name__=="main":
t.setup(960, 540)
t.speed(1)
male(-960/3, 100)
female(960/3, 100)
heart(0, 0)
biu(10,-100)

t.done()

