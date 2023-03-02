def tadaro2(l_in):
    l_end = []
    for letter in l_in:
        is_in = False
        for letter_count in l_end:
            if letter_count[0] == letter:
                is_in = True
                letter_count[1] += 1
        if not is_in:
            l_end.append([letter, 1]) #liste car tuple est immuable
    return [tuple(tpl) for tpl in l_end]
            


print(tadaro2(["a", "c", "c", "c", "o", "e", "a", "i"]))
