import turtle as t, math, time, random

color = ['red', 'yellow', 'green', 'violet', 'indigo', 'blue', 'orange']
###########################################################################################################################
t.hideturtle()
t.speed(30)
t.pensize(25)
###########################################################################################################################
t.up();   t.goto(-300, 0);  t.down();
for i in range (0, 720, 1):
    t.color(color[random.randint(0, 6)])
    t.goto(i*.8 - 300, math.sin(math.radians(i))*120)
time.sleep(5)