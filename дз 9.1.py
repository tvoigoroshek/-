import turtle
t= turtle.Pen()
t.forward(100)
t.right(90)
t.forward(80)
t.left(90)
t.forward(120)
t.right(90)
t.right(360)
t.forward(90)
t.right(90)
t.forward(120)
def circle(red,green,blue):
    t.color(red,green,blue)
    t.begin_fill()
    t.circle(40)
    t.end_fill()
circle(0,0,0)
t.forward(180)
circle(0,0,0)
t.forward(100)
t.right(90)
t.forward(90)
t.right(90)
t.forward(60)
t.left(90)
t.forward(80)
t.right(90)
t.forward(120)


