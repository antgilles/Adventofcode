from  adventofcode10_2 import gethash

nbgrp = 0

def parseneighbour(x,y):
    global nbgrp
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
    ret = list()
    for y in range(128):
        h = gethash(phrase + '-' + str(y))
        print(h)
        line = ''.join(["{:04b}".format(int(i,16)) for i in h]) 
        print(len(line))
        ret.append(line)
    return ret



phrase = 'jzgqcdpd'
phrase = 'flqrgnkx'

matr = phrastomatrix(phrase)
#matr = [[1,1,0],
#       [1,0,1],
#      [0,1,1]]
print(matr)
print(matr[127][127])

visited = set()
moves = [(0,1),(0,-1),(1,0),(-1,0)]
for y in range(len(matr)):
    for x in range(len(matr)):
        #print('parsing : %s %s => %s' % (x,y, matr[x][y]))
        if matr[x][y] == "1" and (x,y) not in visited:
            nbgrp += 1
            visited.add((x,y))
            q = [(x,y)]
            while q:
                x,y = q.pop()
                for dx, dy in moves:
                    nx , ny = x + dx, y + dy
                    if 0 <= nx < len(matr) and  0 <= ny < len(matr) and matr[nx][ny] == "1" and (nx,ny) not in visited:
                        #print('parsing IN: %s %s => %s' % (nx,ny, matr[nx][ny]))
                        visited.add((nx,ny))
                        q.append((nx,ny))





#print(matr)

print(nbgrp)
