from turtle import *

speed(0)

def fivesquares():
    def square(pos:tuple, lenght:int, col:str):
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

    square((0, 0), 20, "yellow")
    square((-200, 200), 50, "blue")
    square((-200, -200), 15, "green")
    square((200, -200), 25, "pink")
    square((200, 200), 30, "red")

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

def fullsquares1():

    def carre_n(col_n):
        begin_fill()
        color(col_n)
        for i in range(4):
            fd(30)
            lt(90)
        end_fill()
        return carre_n

    def carre_b(col_b):
        begin_fill()
        color(col_b)
        for i in range(4):
            fd(30)
            lt(90)
        end_fill()
        return carre_b

    def ligne(col_b,col_n):
        for i in range(7):
            print(carre_b(col_b))
            fd(30)
            print(carre_n(col_n))
            fd(30)
        print(carre_b(col_b))
        fd(30)
        return ligne

    def damier():
        for i in range(7):
            print(ligne("black","white"))
            rt(180)
            print(ligne("white","black"))
            lt(90)
            fd(60)
            lt(90)
        print(ligne("black","white"))
        pencolor("black")
        left(180)
        for i in range(4):
            fd(30*15)
            rt(90)
        return damier

    up()
    goto(-250,250)
    down()
    damier()

# fullsquares1()

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

def fulltriangles1():
    up()
    goto(-250,0)
    down()
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
    for x in range(15):
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
            
# fulltriangles1()

exitonclick() # Cette fonction sert a laisser la page turtle ouverte. Pour la fermer il suffit de cliquer à n'importe quel endroit sur la page turtle.