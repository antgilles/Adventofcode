import re

liste = list('abcdefghijklmnop')

with open('advent16.txt') as f:
    cmdlist = f.readlines()[0].strip().split(',')

print(cmdlist)
for cmd in cmdlist:
    terms = cmd.split('/')
    if terms[0][0] == 's':
        liste = liste[-int(terms[0][1]):] + liste
        del liste[-int(terms[0][1]):]
        print(liste)
    if terms[0][0] == 'x':
        swap = liste[int(terms[0][1])]
        liste[int(terms[0][1])] = liste[int(terms[1])]
        liste[int(terms[1])] = swap
        print(liste)
    if terms[0][0] == 'p':
        rep1 = [i for i,x in enumerate(liste) if x==terms[0][1]]
        rep2 = [i for i,x in enumerate(liste) if x==terms[1]]
        for i in rep1:
            liste[i]=terms[1]
        for i in rep2:
            liste[i]=terms[0][1]
        print(liste)
print(''.join(liste))
