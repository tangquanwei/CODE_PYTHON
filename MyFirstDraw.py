import turtle as t
print("这是我用turtle画的第一个画：")
length = 50
while length <= 250:
    if length<250:
        print("这是第{:.0f}圈".format(length/50))
    else:
        print("这是最后一圈啦！")
    length += 50
    t.penup()
    t.goto(0, -length)
    t.pendown()
    t.pensize(8)
    t.pencolor("yellow")
    t.circle(length, 360)
    t.pensize(2)
    t.pencolor("blue")
    t.goto(length/2*1.732, length/2)
    t.goto(-length/2*1.732, length/2)
    t.goto(0, -length)
    t.penup()
    t.goto(0, length)
    t.pendown()
    t.goto(-length/2*1.732, -length/2)
    t.goto(length/2*1.732, -length/2)
    t.goto(0, length)
    t.pencolor("red")
    t.penup()
    t.goto(0, -length)
    t.pendown()
    t.circle(length, -360)
print("ok可以把它叉掉了\n")
t.done()
# print("你是第一个跟我分享它的人噢！\n")
