def lettres_mot(mot):
    return [l for l in mot if l not in "-'"]

# print(lettres_mot("1019192029"))


def dec_bin(nb):
    t = int(str(nb), 2)
    return t

# print(dec_bin(10000))


def dec_bin1(nb):
    b = ""
    while nb // 2 != 0:
        b = str(nb%2) + b
        nb //= 2
    b = str(nb%2) + b
    return b


# print(dec_bin1(16))

def tab_chiffre(nb):
    return lettres_mot(dec_bin1(nb))

# print(tab_chiffre(16))

def tab_chiffre1(nb):
    return lettres_mot(bin(nb))[2:]

# print(tab_chiffre1(16))

import turtle as tl
tl.speed(100)

def decime_binaire(nb: int): # fonction principale

    def dec_bin2(nb): # fonction qui retourne le binaire (sans 0b) d'un décimal
        b = ""
        while nb // 2 != 0:
            b = str(nb%2) + b
            nb //= 2
        b = str(nb%2) + b
        return b


    def ca(color): # fonction qui dessine le carré de couleur donnée
        tl.begin_fill()
        tl.fillcolor(color)
        for c in range(4):
            tl.fd(20)
            tl.lt(90)
        tl.fd(20)
        tl.end_fill()

    tl.up()
    tl.goto(-250,0)
    tl.down()

    for i in dec_bin2(nb): # boucle qui parcours le binaire
        if i == "0":
            ca("black")
        else:
            ca("white")

# decime_binaire(123)
# print(bin(123))



def decime_hexa(nb: int): # fonction principale

    def ca(color, l): # fonction qui dessine le carré de couleur donnée
        tl.begin_fill()
        tl.fillcolor(color[0])
        for c in range(3):
            tl.fd(50)
            tl.lt(90)
        tl.fd(40)
        tl.pencolor(color[1])
        tl.write("   " + l,font=("Verdana",15, "normal"))
        tl.pencolor("black")
        tl.fd(10)
        tl.lt(90)
        tl.fd(50)
        tl.end_fill()

    tl.up()
    tl.goto(-250,0)
    tl.down()

    for i in hex(nb).replace("0x", ""):
        d = {"0":("black", "white"), "1":("white", "black"), "2":("blue", "white"), "3":("yellow", "black"), "4":("red", "white"), "5":("green", "white"), "6":("pink", "black"), "7":("purple", "white"), "8":("dark blue", "white"), "9":("grey", "black"), "a":("brown", "white"), "b":("cyan", "black"), "c":("yellow", "black"), "d":("red", "white"), "e":("green", "white"), "f":("pink", "black")}
        ca(d[i], i)

decime_hexa(81985529216486895)
print(hex(81985529216486895))

tl.exitonclick()
print(0x0123456789abcdef)
