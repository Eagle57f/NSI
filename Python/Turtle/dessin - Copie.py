import turtle as tl
import random as rd

tl.speed(0)
tl.bgcolor("black")
tl.hideturtle()


def poly(color = "white", length = 30, coos = (0, 0), pnbr=3, w=2):

    tl.pencolor(color)
    tl.up()
    tl.goto(coos)
    tl.down()
    tl.width(w)
    for i in range(pnbr):
        tl.fd(length)
        tl.lt(360/pnbr)


def dessin(coos):
    for coo in coos:
        color = rd.choice(["white", "blue", "yellow", "green", "purple"])
        length = rd.randint(3, 7) * 10
        nbr = rd.randint(4, 15)
        pnbr = rd.randint(3, 10)
        w = rd.randint(1,5)
        for i in range(nbr):
            poly(color, length, coo, pnbr, w)
            tl.lt(360/nbr)

    tl.up()
    y = 0
    tl.goto(-20, y)
    tl.down()
    
    for t in "😀":
        if t == "\n":
            y-=50
            tl.up()
            tl.goto(-20, y)
            tl.down()
        color = rd.choice(["white", "blue", "yellow", "green", "purple"])
        tl.color(color)
        tl.up()
        tl.write(t, move = True, font=('MT',30,'underline'))
        tl.down()



dessin(
((-200,-200),
(200,200),
(200,-200),
(-200,200))
)
tl.exitonclick()