import collections

number=30000
x=0
y=0
lastlen=1
cap=[(1,0),(0,1),(-1,0),(0,-1)]
last=collections.OrderedDict({'0,0': 1})

def getarround(x,y):
    ret = 0
    for arroundx in [-1,0,1]:
        for arroundy in [-1,0,1]:
            if not (arroundx == 0 and arroundy == 0):
                #print('%s,%s' % (x + arroundx, y + arroundy))
                if '%s,%s' % (x + arroundx, y + arroundy) in last:
                    #print('%s,%s => %s' % (x + arroundx, y + arroundy, last['%s,%s' % (x + arroundx, y + arroundy)]))
                    ret += last['%s,%s' % (x + arroundx, y + arroundy)]
    return ret

direction=0
directionlen=0

countdir = 0
for i in range(1,number + 1):
    x += cap[direction][0]
    y += cap[direction][1]
    countdir += 1
    print ("x=%s" % x)
    print ("y=%s" % y)
    if countdir == lastlen:
        countdir=0
        direction += 1
        if direction == 2:
            lastlen += 1
        if direction == 4:
            direction = 0
            lastlen += 1

    last['%s,%s' % (x,y)] = getarround(x,y)
    print(last)

    print('%s: %s,%s,lastlen %s, dir %s, countdir %s' % (i,x,y,lastlen,direction,countdir))

    if len(last) > 1000:
        last.popitem()

    if last['%s,%s' % (x,y)] > 325489:
        print(last['%s,%s' % (x,y)])
        break
