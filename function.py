#Create a polygon function that accepts a turtle, sides, and distance.
#function file
#Don't change my file U!!!!!!!!!!!!!!!

def polygon(t,s,d):#parameters(information)
    a=360/s#angle variable is inside the function
    for times in range(s):
        t.forward(d)
        t.left(a)

def polygonfill(t,s,d,c):
    a=360/s
    t.color(c)
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.left(a)
    t.end_fill()

def jump(t,x,y):#parameters
    t.penup()
    t.goto(x,y)
    t.pendown()

def cool(t,d,c1,c2):#parameter
    t.color(c1)
    polygon(t,4,d)#csll to the function polygon
    t.color(c2)
    polygon(t,3,d)

def star(t,d,c):
    t.begin_fill()
    t.color(c)
    for times in range(8):
        t.forward(d)
        t.left(135)
    t.end_fill()

def star1(t,d,c):
    t.pencolor(c)
    for times in range(8):
        t.forward(d)
        t.left(135)
        
def stars(t,c):
    for times in range(11):
        star(t,times *10 + 8,c)
        t.penup()
        t.right(30)
        t.forward(50)
        t.pendown()
