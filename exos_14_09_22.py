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



