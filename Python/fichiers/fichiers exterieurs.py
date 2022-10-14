with open(r"D:\1ere\NSI\Python\texte.txt", "r", encoding="UTF-8") as f:
    f = f.readlines()
    n = 1
    go = False
    txt = []
    for line in f:
        if f.index(line) not in [23, 4, 3, 2, 1, 0]: # 0,1,2,3,4 sont les titres du sonnet, 5 est une ligne vide
            go = True
            print(n, ": ", line, end="")
            txt.append(str(n) + ": " + line)
            n+=1
        elif line == "\n" and go == True:
            print("")
            txt.append("\n")


with open(r"D:\1ere\NSI\Python\texte1.txt", "w", encoding="UTF-8") as f:
    f.writelines(txt)


