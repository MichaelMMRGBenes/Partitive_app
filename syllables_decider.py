def syllables_decider(word):
    vowels = "aeiouyäö"
    diphthongs = {"ai","ei","oi","ui","yi","äi","öi","au","eu","iu","ou","äy","öy","ey","iy","ie","uo","yö","io"}

    word = word.lower()
    count = 0
    i = 0

    while i < len(word):
        if word[i] in vowels:
            count += 1
            if i+2 < len(word) and word[i+1:i+3] in diphthongs:
                i += 1
            elif i+1 < len(word) and (word[i] == word[i+1] or word[i:i+2] in diphthongs):
                i += 1
        i += 1
    return count

x = (syllables_decider("puu"))
print(x)