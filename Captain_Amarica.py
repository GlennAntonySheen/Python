import turtle as t, math, time
color = ["red", "white", "red", "blue"]

t.speed(6)

def go(y):
    t.penup()
    t.goto(0, y)
    t.pendown()
    t.begin_fill()
    t.circle(abs(y))
    t.end_fill()

for i in range(4):
    t.color(color[i])
    go(-200 + (i * 35))

t.penup()
t.goto(0, 70)
t.pendown()
t.begin_fill()
t.color('white')
t.rt(90-18)

for i in range(5):
    t.fd(50)
    t.lt(72)
    t.fd(50)
    t.rt(144)
t.end_fill()    

t.hideturtle()
time.sleep(4)
