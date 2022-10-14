#Ecrire une fonction nbr_lettre ayant pour paramètre un tab_mot qui est un tableau de mots et qui retourne tab_nbr contenant le nombre de lettres de chaque mot
def nbr_lettre(tab_mot):
    tab_nbr=[len(mot) for mot in tab_mot]
    return tab_nbr

# print(nbr_lettre(["je","suis","mort",""]))


# écrire une fonction trois_lettre ayant pour paramètre un tableau de mot et qui retourne le tableau_lettre contenant la 3eme lettre de chaque mot du tableau
def trois_lettre(tab):
    tableau_lettre=[elt[2] for elt in tab if len(elt)>=3]
    return tableau_lettre
        
# print(trois_lettre(['demain','hier','moi','de']))


# Ecrire une fonction element ayant pour paramètre tab et qui print("le premier element de tab est") print("le deuxième element de tab est") etc...
def element(tab):
    if len(tab) != 0:
        for i in range(len(tab)):
            print("le", i+1, "eme élément de tab:", tab[i])
            # ou sinon print(f"le {i+1}eme élément de tab:{tab[i]}")
    else :
        print("Le tableau est vide")

# element(['demain','hier','moi','de'])


#Ecrire une fonction tab_mult ayant pour paramètre un nombre et qui retourne le tab_n qui est la table de multiplication de se nombre
def tab_mult(nbr):
    tab_n = [ nbr*i for i in range(11)]
    return tab_n

# print(tab_mult(8))


def tab_mult_en_tableau(nbr):
    line_tab = [f"""|  {nbr} x {i}  {" " if i < 10 else ""}  {" " if nbr < 10 else ""}|     {nbr*i} {" " if nbr*i < 10 else ""}  |""" for i in range(11)]

    print("--------------------------")
    for line in line_tab:
        print(line)
    print("--------------------------")

tab_mult_en_tableau(8)
