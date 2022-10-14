import turtle as tl
tl.speed(0)
tl.bgcolor("#c2fffe")

def decime_binaire(nombre: int): # fonction principale

    def dec_bin2(nombre): # fonction qui retourne le binaire (sans 0b) d'un décimal
        b = ""
        while nombre // 2 != 0:
            b = str(nombre%2) + b
            nombre //= 2
        b = str(nombre%2) + b
        return b


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

    for i in dec_bin2(nombre): # boucle qui parcours le binaire
        if i == "0":
            ca(("black", "white"), "0")
        else:
            ca(("white", "black"), "1")

decime_binaire(71579)
print(bin(71579))

def decime_hexa(nombre: int): # fonction principale

    def ca(color, l): # fonction qui dessine le carré de couleur donnée (color[0]), avec la couleur du texte (color[1])
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
    tl.goto(-250,-75)
    tl.down()

    for i in hex(nombre).replace("0x", ""): # boucle qui parcours le hexadecimal
        d = {
        "0":("black", "white"),
        "1":("white", "black"),
        "2":("blue", "white"),
        "3":("yellow", "black"),
        "4":("red", "white"),
        "5":("green", "white"),
        "6":("pink", "black"),
        "7":("purple", "white"),
        "8":("dark blue", "white"),
        "9":("grey", "black"),
        "a":("brown", "white"),
        "b":("cyan", "black"),
        "c":("orange", "black"),
        "d":("dark red", "white"),
        "e":("dark green", "white"),
        "f":("dark grey", "black")}
        ca(d[i], i)

decime_hexa(81985529216486895)
print(hex(81985529216486895))

tl.exitonclick()