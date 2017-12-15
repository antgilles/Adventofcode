
liste = [i for i in range(256)]
print(liste)

length = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]
#length = [3, 4, 1, 5]
pos = 0
skip = 0

for i in length:
    #print(liste)
    posend = (pos + i ) % len(liste)
    print("pos: %s,  posend: %s, len: %s, skip :%s" % (pos, posend, i, skip))

    if posend <= pos:
        rep = list(liste[pos:]) + list(liste[:posend])
    else:
        rep = list(liste[pos:posend])
    rep.reverse()
    for j in range(len(rep)):
        liste[(pos + j) % len(liste)] = rep[j]
    pos = (posend + skip) % len(liste)
    skip += 1

print(liste)

print(liste[0] * liste[1])
