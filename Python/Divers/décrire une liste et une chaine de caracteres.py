'''ecrire une fonctino mult_3 ayant comme parametre une liste de nombres entierts qui s appellent tab qui retourne  une liste appelée tab_mult3, tableau des elements de tab qui sont des multiples de 3'''


def mult_3(tab):
    tab_mult3 = [item for item in tab if item % 3 == 0]
    return tab_mult3

print("exo1:", mult_3([0,1,2,3,4,5,6,7,8,9,10]))


'''ecrire une fonction nombre_lettre ayant pour parametre un mot et qui retourne le nombre de lettres lettre du mot'''

def nombre_lettre_mot(mot):
    return len(mot)

print("exo2:", nombre_lettre_mot("salut"))

def nombre_lettre_phrase_tktfrr(phrase):
    t = phrase
    phrase.split()
    return len([item for item in t if item in "abcdefghijklmnopqrstuvwxyzéèêàùûâöôç"])

print("exo3,1:", nombre_lettre_phrase_tktfrr("salut, je suis    t"))

def nombre_lettre_phrase(phrase):
    nb_letter = 0
    for word in phrase.split():
        nb_letter += len([letter for letter in word if letter in "abcdefghijklmnopqrstuvwxyzéèêàùûâöôç"])
    return nb_letter

print("exo3,2:", nombre_lettre_phrase("salut, je suis    t"))

def nombre_lettre_phrasetktfrr2(phrase):
    t=""
    for word in phrase.split():
        t+=word
    
    return len([letter for letter in t if letter in "abcdefghijklmnopqrstuvwxyzéèêàùûâöôç"])

print("exo,3:", nombre_lettre_phrasetktfrr2("salut, je suis    t"))
