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



