import os

with open("advent11.txt") as f:
    lines = [i.strip() for i in f.readlines()]

directions = lines[0].split(',')

print(directions)

dicodir = {'n':(0,2), 'ne':(1,1), 'se':(1,-1), 's':(0,-2), 'sw':(-1,-1), 'nw':(-1,1)}

x=0
y=0
result = 0

for i in directions:
    x += dicodir[i][0]
    y += dicodir[i][1]
    print('x=%s , y=%s' %(x,y))

    if abs(x) > abs(y):
        tmp = abs(x)
    else:
        tmp = abs(x) + (abs(y) - abs(x))/2

    if tmp > result:
        result = tmp

#if abs(x) > abs(y):
#    result = abs(x)
#else:
#    result = abs(x) + (abs(y) - abs(x))/2

print(result)
