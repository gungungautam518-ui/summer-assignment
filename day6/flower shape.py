import turtle


a=turtle.Turtle()
a.color("red","yellow")
a.begin_fill()
a.speed(8)

for i in range(24):
    a.forward(300)
    a.right(165)
a.end_fill()   
turtle.done()    
