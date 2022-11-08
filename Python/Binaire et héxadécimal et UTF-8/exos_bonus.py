# Exo 1
def ASCII_lettre(car):
    return bin(ord(car))[2:]

print(ASCII_lettre("!"))



# Exo 2

def ASCII_mot(mot):
    bina=[]
    for lettre in mot:
        x=[lettre for lettre in bin(ord(lettre))[2:]]

        bina.extend(["".join(x), "\\"])
        
    return "".join(bina[:-1])


# Exo 3, 4 et 5

def ASCII_phrase(phrase):
    bina=[]
    phrase = phrase.split(" ")
    for mot in phrase:
        for lettre in mot:
            x=[l for l in bin(ord(lettre))[2:]]
            bina.extend("".join(x))

        bina.append(" ")


    return "".join(bina)[:-1]


def ph_binaire(phrase): # fonction principale

    import turtle as tl
    tl.speed(0)
    tl.bgcolor("#c2fffe")

    b = ASCII_phrase(phrase)


    def carre(color, l): # fonction qui dessine l'héxagone de couleur donnée
        tl.begin_fill()
        tl.fillcolor(color[0])
        tl.lt(30)
        for c in range(5):
            tl.fd(20)
            tl.lt(60)
        tl.fd(4)
        tl.pencolor(color[1])
        tl.write("   " + l,font=("Verdana",15, "normal"))
        tl.pencolor("black")
        tl.fd(16)
        tl.rt(30)
        tl.up()
        tl.lt(60)
        tl.fd(36)
        tl.down()
        tl.end_fill()


    tl.up()
    tl.goto(-250,200)
    tl.down()

    j = 0
    yp = 200
    
    for i in b: # boucle qui parcours le binaire
        
        if j >= 10:
            yp -= 38
            tl.up()
            tl.goto(-250, yp)
            tl.down()
            j=0
        j += 1
        if i == "0":
            carre(("black", "white"), "0")
        elif i == "1":
            carre(("white", "black"), "1")
        else:
            tl.up()
            tl.fd(36)
            tl.down()

    tl.exitonclick() 

ph_binaire("Codage ASCII")




# Question bonus

def fichier():
    with open(r"Python\Binaire et héxadécimal et UTF-8\sauvegarde.txt", "w") as f:
        f.write(ASCII_phrase("Codage ASCII"))
