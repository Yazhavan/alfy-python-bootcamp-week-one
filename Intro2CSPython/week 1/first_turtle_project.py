import turtle

def rectangle(edge=100):
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)

rectangle()
def circle1(edge=100):
    turtle.circle(35)
    turtle.circle(19)
circle1()
turtle.forward(100)
circle1()

def circle2(edge=100) :
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.circle(13)
    turtle.penup()
    turtle.forward(20)


circle2()

def circle3(edge=100):
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(17)


circle3()
turtle.left(180)
circle2()

turtle.left(90)
turtle.penup()
turtle.forward(32)

turtle.pendown()

turtle.circle(45,extent=180)



















turtle.mainloop()
