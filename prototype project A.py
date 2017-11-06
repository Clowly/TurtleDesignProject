#Prototype project
import turtle
alice=turtle.Turtle()
turtle.colormode(255)
from function import*
from random import*
turtle.bgcolor("black")
alice.speed(0)

for times in range(254):
    c=(0,times,255)
    alice.pencolor()
    alice.color(c)
    alice.circle(times)
    alice.right(135)

jump(alice,0,0)

for times in range(357):
    c=(255,0,127)
    alice.pencolor()
    alice.color(c)
    polygon(alice,4,times)
    alice.right(135)

for times in range(50):
    c=(128,128,128)
    y=randint(2,8)
    alice.begin_fill()
    for times in range(8):
        alice.color(c)
        alice.circle(y)
    jump(alice,randint(-1000,1000),randint(-500,500))
    alice.end_fill()

for times in range(50):
    c=(100,100,100)
    y=randint(2,8)
    alice.begin_fill()
    for times in range(8):
        alice.color(c)
        alice.circle(y)
    jump(alice,randint(-900,900),randint(-500,500))
    alice.end_fill()
    
for times in range(50):
    c=(255,255,255)
    y=randint(2,8)
    alice.begin_fill()
    for times in range(8):
        alice.color(c)
        alice.circle(y)
    jump(alice,randint(-800,800),randint(-500,500))
    alice.end_fill()

jump(alice,0,0)

for times in range(38):
    alice.pencolor(255,255,0)
    polygon(alice,3,400)
    alice.right(10)


jump(alice,600,400)

for times in range(40):
    star1(alice,50,(255,255,0))
    alice.right(10)

jump(alice,-600,400)

for times in range(40):
    star1(alice,50,(255,255,0))
    alice.right(10)

jump(alice,-600,-400)

for times in range(40):
    star1(alice,50,(255,255,0))
    alice.right(10)

jump(alice,600,-400)

for times in range(40):
    star1(alice,50,(255,255,0))
    alice.right(10)

for times in range(50):
    y=randint(8,10)
    star1(alice,y,(204,0,204))
    jump(alice,randint(-800,800),randint(-500,500))
