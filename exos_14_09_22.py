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

def somme_hexa(n, m):
    if type(n) is str:
        n = int(n,16)
    if type(m) is str:
        m = int(m,16)
    number = n + m

    hex_num = ""
    def tohex(number, hex_num, b):
        nb=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        if number<=1:
            hex_num = str(number) + hex_num
            b = True
        else:
            x = number%16
            number = number//16
            if x < 10:
                hex_num = str(x) + hex_num
            if x >= 10:
                hex_num = str(nb[x]) + hex_num
        return number, hex_num, b
    b = False
    while number//16 != 0 and b == False:
        number, hex_num, b = tohex(number, hex_num, b)
    number, hex_num, b = tohex(number, hex_num, b)

    return hex_num


print(somme_hexa("0x1f04d", 0x561f1a)) # Prend en paramètres des hexadécimaux, strings avec 0x ou sans.