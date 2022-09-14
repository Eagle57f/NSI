###"Exercice 1######


####Effectuer en système hexadécimal les sommes suivantes:
####  afe125+de15f et vérifiez votre résultat sur python
####  bdcfe15+abc36f

# print(hex(0xafe125+0xde15f)) # bdc284

# print(hex(0xbdcfe15+0xabc36f)) # c88c184



###Exercice 2####
### Ecrire une fonction dec_bin ayant pour paramètre nombre et qui
### retourne la chaine de caractères binaire qui est l'écriture binaire du nombre

def dec_bin(nombre:int):
    bin_nb = ""
    while nombre//2 != 0:
        bin_nb = str(nombre%2) + bin_nb
        nombre //= 2
    bin_nb = str(nombre%2) + bin_nb
    return bin_nb

# print(dec_bin(1234)) # 10011010010
# print(bin(1234)) # 10011010010

### dec_bin(16) donne 10000
### pour tester bin (16)=0b10000

# print(dec_bin(16)) # 10000

###Exercice 3####
###même exercice que 2 mais la fonction dec_bin_tab retourne un tableau contenant
###dans l'ordre les chiffres de l'écriture de nombre en binaire
##"on pourra utiliser l'exercice2

def dec_bin1(nombre:int):
    bin_nb = []
    while nombre//2 != 0:
        bin_nb.insert(0, str(nombre%2))
        nombre //= 2
    bin_nb.insert(0, str(nombre%2))
    return bin_nb

# print(dec_bin1(1234)) # ['1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0']
# print(bin(1234)) # 10011010010



###Exercice 4 ####
###Ecrire une fonction somme_hexa ayant pour paramètre deux nombres n et m
### m et n sont des nombres en hexadécimal
### somme_hexa doit retourner la somme de n et m en héxadécimal.


def hex_hex(n: str, m: str):
    n = str(hex(n)).replace("0x","")
    m = str(hex(m)).replace("0x","")
    nb=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    hex_nb = ""
    for i in range(max([len(n)-2, len(m)-2])):
        hex_nb = str(nb.index(n[i])) + str(nb.index(m[i])) + hex_nb
    
    return hex_nb

print(hex_hex(0x1f2f4d,0x1))