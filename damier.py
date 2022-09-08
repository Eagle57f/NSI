from turtle import*
bgcolor("black")

speed(0)
ht()


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

def ligne_(col_b,col_n):
    for i in range(7):
        print(carre_b(col_b))
        fd(30)
        print(carre_n(col_n))
        fd(30)
    print(carre_b(col_b))
    fd(30)
    return ligne

def damier(col_b,col_n):
    for i in range(7):
        print(ligne("white","red"))
        rt(180)
        print(ligne("red","white"))
        lt(90)
        fd(60)
        lt(90)
    print(ligne("white","red"))
    return damier

up()
goto(-250,250)
down()
print(damier("white","red"))
        
































