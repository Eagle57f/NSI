with open(r"D:\1ere\NSI\Python\NSI_fic.txt", "r", encoding="UTF-8") as f:
    nb_mot = nb_lettre = nb_ligne = nb_voy = nb_cons = 0


    for ligne in f:
        nb_ligne +=1
        for car in ligne:
            if car.lower() in "abcdefghijklmnopqrstuvwxyzéèêàùûâöôç":
                nb_lettre += 1
                if car.lower() in "aeiouyéèêàùûâ":
                    nb_voy += 1
                else:
                    nb_cons +=1

        ligne = ligne.split()
        nb_mot+= len(ligne)
        
    print(
f"""Le nombre de lignes dans ce texte est de : {nb_ligne},
Le nombre de mots dans ce texte est de : {nb_mot},
Le nombre de lettres dans ce texte est de : {nb_lettre},
Le nombre de voyelles dans ce texte est de {nb_voy},
Le nombre de consonnes dans ce texte est de {nb_cons},
Le pourcentage de consonnnes dans ce texte est de environ : {round(nb_cons/nb_lettre*100, 2)} %,
Le pourcentage de voyelles dans ce texte est de environ : {round(nb_voy/nb_lettre*100, 2)} %"""
    )