
liste = [i for i in range(256)]
#liste = [i for i in range(5)]
print(liste)

length = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]
#length = [5]
pos = 0
skip = 0

for i in length:
    print(liste)
    posend = (pos % len(liste) + i )
    print("pos: %s,  posend: %s, len: %s, skip :%s" % (pos, posend, i, skip))

    if posend > len(liste):
        rep = list(liste[pos % len(liste):]) + list(liste[0:posend % len(liste)])
    else:
        rep = list(liste[pos % len(liste):posend])
    print(rep)
    rep.reverse()
    print(rep)
    for j in range(len(rep)):
        print("replacing char %s par %s" %((pos +j) % len(liste), rep[j]))
        liste[(pos % len(liste)+ j) % len(liste)] = rep[j]
    pos = (pos + i + skip)
    skip += 1
    print(liste)

print(liste)

print(liste[0] * liste[1])
