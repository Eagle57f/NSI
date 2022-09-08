from turtle import *

speed(100)

def fivesquares():
    def square(*, pos:tuple, lenght:int, col:str):
        up()
        goto(pos)
        down()
        begin_fill()
        for i in range(4):
            fillcolor(col)
            pencolor(col)
            fd(lenght)
            lt(90)
        end_fill()

    square(pos=(0, 0), lenght=20, col="yellow")
    square(pos=(-200, 200), lenght=50, col="blue")
    square(pos=(-200, -200), lenght=15, col="green")
    square(pos=(200, -200), lenght=25, col="pink")
    square(pos=(200, 200), lenght=30, col="red")

    exitonclick()

# fivesquares()


def fullsquares():
    def square(col):
        down()
        begin_fill()
        fillcolor(col)
        for i in range(4):
            fd(30)
            lt(90)
        end_fill()
        up()

    up()
    goto(-200,-220)
    down()
    for i in range(4):
        fd(30*15)
        left(90)

    for y in range(15):
        up()
        goto(-200,200-y*30)
        down()
        if y%2==0:
            square("black")
        for x in range(7):
            if y%2==0:
                fd(60)
                square("black")
            else:
                fd(30)
                square("black")
                fd(30)
    exitonclick()

# fullsquares()

def fullpolys():
    def poly(sides, lenght, *,x,y,color:str):
        pencolor(color)
        up()
        goto(x,y)
        down()
        for i in range(sides):
            forward(lenght)
            right(360 / sides)
        

    poly(8,20,x=0,y=0, color="blue")
    poly(4,20,x=-150,y=150, color="green")
    poly(6,20,x=-150,y=-150, color="yellow")
    poly(12,20,x=150,y=-150, color="pink")
    poly(3,20,x=150,y=150, color="red")
    exitonclick()

# fullpolys()



def fulltriangles():
    def triangle(col):
        down()
        pencolor("black")
        begin_fill()
        fillcolor(col)
        for i in range(3):
            fd(30)
            lt(120)
        end_fill()
        up()
    for x in range(7):
        if x%2==0:
            up()
            fd(30)
            down()
            triangle("black")

        else:
            up()
            fd(30)
            down()
            triangle("white")
            
fulltriangles()
exitonclick()
