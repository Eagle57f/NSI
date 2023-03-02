def recherche(c, mot):
    i=0
    for car in mot:
        if car == c:
            i+=1
    print(i)
    return i

# recherche("a", "mississipi")


def recherche2(c, mot):
    return len([car for car in mot if car == c])

# print(recherche2("a", "Alibaba"))



def moyenne(list_notes):
    somme_notes = 0
    somme_coeffs = 0
    for note in list_notes:
        somme_notes += (note[0] * note[1])
        somme_coeffs += note[1]
    
    return "Absent" if not somme_notes == 0 else somme_notes/somme_coeffs

# print(moyenne([(15,2), (9,1), (12,3)]))
# print(moyenne([]))


def moyenne2(list_notes):
    somme_notes = sum([note[0] * note[1] for note in list_notes])
    somme_coeffs = sum([note[1] for note in list_notes])
    
    return "Absent" if somme_notes == 0 else somme_notes/somme_coeffs

# print(moyenne2([(15,2), (9,1), (12,3)]))
# print(moyenne2([]))



def recherche3(list_t):
    list_res = []
    for i in range(len(list_t)-1):
        if list_t[i+1]-1 == list_t[i]:
            list_res.append((list_t[i], list_t[i+1]))
    return list_res

# print(recherche3([1,2,3,4,2,5,9,3,1]))


def recherche4(list_t):
    return [(list_t[i], list_t[i+1]) for i in range(len(list_t)-1) if list_t[i+1]-1 == list_t[i]]

# print(recherche4([1,2,3,2,4,2,5,9,3,1]))




def tadaro(l):
    d = {}
    for letter in l:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    l_end = []
    for letter in d:
        l_end.append((letter, d[letter]))
    return l_end


# print(tadaro(["a", "c", "c", "c", "o", "e", "a", "i"]))





def tadaro2(l):
    l_end = []
    for letter in l:
        is_in = False
        for letter_count in l_end:
            if letter_count[0] == letter:
                is_in = True
                letter_count[1] += 1
                break
        if is_in == False:
            l_end.append([letter, 1]) #liste car tuple est immuable
    return [tuple(tpl) for tpl in l_end]
            


print(tadaro2(["a", "c", "c", "c", "o", "e", "a", "i"]))







def trop_long(li):
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    for letter in li:
        if letter == "a": a+=1
        if letter == "b": b+=1
        if letter == "c": c+=1
        if letter == "d": d+=1
    l_end = []
    if a > 0: l_end.append(("a", a))
    if b > 0: l_end.append(("b", b))
    if c > 0: l_end.append(("c", c))
    if d > 0: l_end.append(("d", d))

    return l_end

# print(trop_long(["a", "c", "c", "c", "d"]))







