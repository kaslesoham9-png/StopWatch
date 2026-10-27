import turtle
import time

# screen
screen = turtle.Screen()
screen.listen()
screen.tracer(0)

# circle
size=150
c = turtle.Turtle()
c.color("gray")
c.hideturtle()
c.begin_fill()
c.sety(c.ycor()-size)
c.circle(size)
c.end_fill()
screen.update()

# rectangle
length, bredth = 175, 75
r = turtle.Turtle()
r.hideturtle()
r.color("black")
r.goto(-length/2,-bredth/2)
r.begin_fill()
r.setx(r.xcor()+length)
r.sety(r.ycor()+bredth)
r.setx(r.xcor()-length)
r.sety(r.ycor()-bredth)
r.end_fill()
screen.update()

# display
d = turtle.Turtle()
d.hideturtle()
d.color("red")
d.sety(d.ycor()-20)

# start stopwatch
condition = False
timer=-1
def run():
    global timer
    if condition:
        d.clear()
        d.write(timer+1,align="center",font=("algerian",32))
        timer+=1
    screen.update()
    screen.ontimer(run,1000)

# restart button
def restart(x,y):
    global timer, condition
    timer=0
    condition=False
    d.clear()
    d.write(timer,align="center",font=("algerian",32))
res = turtle.Turtle()
res.penup()
res.shape("circle")
res.shapesize(3)
res.color("orange")
res.goto(-75,-200)
screen.update()
res.onclick(restart)

# start stop
def startstop(x,y):
    global condition
    condition = not condition
ss = turtle.Turtle()
ss.penup()
ss.shape("circle")
ss.shapesize(3)
ss.color("green")
ss.goto(75,-200)
screen.update()
ss.onclick(startstop)

# texts
text1 = turtle.Turtle()
text1.hideturtle()
text1.penup()
text1.goto(res.xcor(),res.ycor()-55)
text1.write("Reset",align="center",font=("algerian",15))
text2 = turtle.Turtle()
text2.hideturtle()
text2.penup()
text2.goto(ss.xcor(),ss.ycor()-55)
text2.write("Start/Stop",align="center",font=("algerian",15))

# keys
def startstop1():
    startstop(1,1)
def restart1():
    restart(1,1)
def exit0():
    exit()
screen.onkey(startstop1,"s")
screen.onkey(restart1,"r")
screen.onkey(exit0,"q")

run()
turtle.done()