from  adventofcode10_2 import gethash


def parseneighbour(x,y):
    print('parsing: %s %s => %s' % (x,y, matr[x][y]))
    if matr[x][y] == 1:
        matr[x][y] = 2
        if x + 1 < len(matr) :
            parseneighbour(x + 1,y)
        if x - 1 >= 0 :
            parseneighbour(x - 1,y)
        if y + 1 < len(matr) :
            parseneighbour(x,y + 1)
        if y - 1 >= 0 :
            parseneighbour(x,y - 1)

def phrastomatrix(phrase):
    matr = [[0 for i in range(128)] for j in range(128)]
    for y in range(128):
        h = gethash(phrase + '-' + str(y))
        line = "{0:8b}".format(int(h,16))
        for x in range(len(line)):
            if line[x] == '1':
                matr[x][y]= 1
    return matr



phrase = 'jzgqcdpd'
phrase = 'flqrgnkx'

matr = phrastomatrix(phrase)
#matr = [[0,1,0],
#        [1,0,1],
#        [0,1,0]]


nbgrp = 0
for x in range(128):
    for y in range(128):
        print('x = %s' % x)
        print('y = %s' % y)
        print('parsing OUT : %s %s => %s' % (x,y, matr[x][y]))
        if matr[x][y] == 1:
            nbgrp += 1
            print('=====> UP')
            parseneighbour(x,y)

#print(matr)

print(nbgrp)
