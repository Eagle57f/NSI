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


def multiplie2(tabl):
    tabl1=[3*item+4 for item in tabl]
    return(tabl1)

print(multiplie2([1,1.2,-14])) # [7, 7.6, -38]
