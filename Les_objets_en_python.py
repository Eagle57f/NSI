type(1) # <class 'int'> --> integer --> entier

type(1.225691) # <class 'float'> --> float --> flottant

type("bonjour") # <class 'str'> --> string --> chaîne de caractères

type([1,"bonjour", 1.2]) # <class 'list'> --> list --> liste

type((1,2)) # <class 'tuple'> --> tuple --> tuple

type({"first": "bonjour", "second": 2}) # <class 'dict'> --> dictionnary --> dictionnaire


def multiplie(liste):
    tab1=[]
    for item in liste:
        tab1.append(2*item)
    return(tab1)

print(multiplie([1,1.2,-14])) # [2, 2.4, -28]

def multiplie1(liste):
    tab1=[2*item for item in liste]
    return(tab1)

print(multiplie1([1,1.2,-14])) # [2, 2.4, -28]


def multiplie2(tabx):
    tablx1=[3*item+4 for item in tabx]
    return(tablx1)

print(multiplie2([1,1.2,-14])) # [7, 7.6, -38]


def voyelle_mot(mot):
    tab_voy = []
    for letter in mot:
        if letter in "aeiouyAEIOUY":
            tab_voy.append(letter)
    return tab_voy

print(voyelle_mot("Acadabra")) # ['A', 'a', 'a', 'a']


def voyelle_mot1(mot):
    tab_voy = [letter for letter in mot if letter in "aeiouyAEIOUY"]
    return tab_voy

print(voyelle_mot1("Acadabra"))
#ayant pour parametre une phrase appelee phrase et qui retourne le nombre de voyelles et qui retourne le nombre nrb_voy = au nombre de voyelles de la phrase

def nb_voyelle_mot(mot):
    nb_voy = 0
    for letter in mot:
        if letter in "aeiouyAEIOUY":
            nb_voy += 1
    return nb_voy

print(nb_voyelle_mot("Acadabra"))
