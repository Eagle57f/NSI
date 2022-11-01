
# Exo 2

def ASCII_mot(mot):
    bina=[]
    for lettre in mot:
        x=[lettre for lettre in bin(ord(lettre))[2:]]

        bina.extend(["".join(x), "\\"])
        
    return "".join(bina[:-1])


# Exo 5

def ASCII_phrase(phrase):
    bina=[]
    phrase = phrase.split(" ")
    for mot in phrase:
        for lettre in mot:
            x=[l for l in bin(ord(lettre))[2:]]
            bina.extend("".join(x))

        bina.append(" ")


    return "".join(bina)[:-1]



import turtle as tl
tl.speed(0)
tl.bgcolor("#c2fffe")


def ph_binaire(phrase): # fonction principale

    b = ASCII_phrase(phrase)


    def carre(color, l): # fonction qui dessine le carré de couleur donnée
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
    tl.goto(-250,200)
    tl.down()

    j = 0
    yp = 200
    
    for i in b: # boucle qui parcours le binaire
        
        if j >= 10:
            yp -= 60
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
            tl.fd(50)
            tl.down()

# ph_binaire("Codage ASCII")

#tl.exitonclick()


# Question bonus

with open(r"Python\Binaire et héxadécimal et UTF-8\sauvegarde.txt", "w") as f:
    f.write(ASCII_phrase("Codage ASCII"))