
liste = [i for i in range(256)]
liste = [i for i in range(5)]
print(liste)

length = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]
length = [3, 4, 1, 5, 17, 31, 73, 47, 23]
phrase = '1,2,3'

length = [ord(i) for i in phrase] + [17, 31, 73, 47, 23]
print(length)
pos = 0
skip = 0

for i in length:
    print(liste)
    posend = (pos  + i )
    print("pos: %s,  posend: %s, len: %s, skip :%s" % (pos, posend, i, skip))

    if posend > len(liste):
        posend = posend % len(liste)
        rep = list(liste[pos:]) + list(liste[:posend])
    else:
        rep = list(liste[pos:posend])
    print(rep)
    rep.reverse()
    print(rep)
    for j in range(len(rep)):
        print("replacing char %s par %s" %((pos +j) % len(liste), rep[j]))
        liste[(pos % len(liste)+ j) % len(liste)] = rep[j]
    pos = (pos + i + skip) % len(liste)
    skip += 1
    print(liste)

print(liste)

print(liste[0] * liste[1])
