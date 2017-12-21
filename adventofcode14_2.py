from  adventofcode10_2 import gethash

def parseneighbour(x,y):
    if matr[x][y] == "1":
        matr[x][y] = "2"
        if x + 1 < len(matr) :
            parseneighbour(x + 1,y)
        if x - 1 >= 0 :
            parseneighbour(x - 1,y)
        if y + 1 < len(matr) :
            parseneighbour(x,y + 1)
        if y - 1 >= 0 :
            parseneighbour(x,y - 1)

def phrastomatrix(phrase):
    ret = list()
    for y in range(128):
        h = gethash(phrase + '-' + str(y))
        line = list(''.join(["{:04b}".format(int(i,16)) for i in h]))
        ret.append(line)
    return ret



phrase = 'jzgqcdpd'
#phrase = 'flqrgnkx'

matr = phrastomatrix(phrase)

nbgrp = 0
for y in range(len(matr)):
    for x in range(len(matr)):
        #print('parsing : %s %s => %s' % (x,y, matr[x][y]))
        if matr[x][y] == "1":
            nbgrp += 1
            parseneighbour(x,y)

print(nbgrp)
