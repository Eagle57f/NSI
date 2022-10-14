import turtle as tl
import random as rd

tl.speed(0)
tl.bgcolor("black")
tl.hideturtle()


def triangle(color = "white", length = 30, coo = (0, 0)):

    tl.pencolor(color)
    tl.up()
    tl.goto(coo)
    tl.down()
    for i in range(3):
        tl.fd(length)
        tl.lt(120)


def dessin(coos):
    for coo in coos:
        color = rd.choice(["white", "blue", "yellow", "green", "purple"])
        length = rd.randint(3,10) * 10
        nbr = rd.randint(4, 15)
        for i in range(nbr):
            triangle(color, length, coo)
            tl.lt(360/nbr)

    tl.up()
    tl.goto(0, 0)
    tl.down()    
    tl.write("Grun\nNicolas", font=('MT',30,'underline'))    


dessin(
((-200,-200),
(200,200),
(200,-200),
(-200,200))
)
tl.exitonclick()