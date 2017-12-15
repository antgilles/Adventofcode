from itertools import cycle

liste = [i for i in range(5)]
print(liste)

liste=cycle(liste)


length = [3, 4, 1, 5]

pos = 0
skip = 1

for i in length:
    print(liste)
    posend = (pos + i )
    print(pos)
    print(posend)
    rep = list(liste[pos:posend])
    rep.reverse()
    liste[pos:posend]=rep

    pos = posend + skip
    skip += 1
