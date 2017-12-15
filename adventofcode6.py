
memblocks=[int(i) for i in "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3".split()]
#memblocks=[int(i) for i in "0 2 7 0".split()]



history=[list(memblocks),]
print(history)
print(memblocks in history)
result=0
while 1:
    #print ("===> %s" % memblocks)
    result +=1
    maxi = 0
    maxpos = 0
    for i in range(len(memblocks)):
        if memblocks[i] > maxi:
             maxi = memblocks[i]
             maxpos = i
    #print('max = %s / pos = %s' % (maxi, maxpos))
    memblocks[maxpos]=0
    for i in range(1,maxi + 1):
        memblocks[(maxpos + i) % len(memblocks)] += 1
        #print ("rearange en cours : %s" % memblocks)
    #print(history)
    if memblocks in history:
        print(result)
        print(result - history.index(list(memblocks)))
        break
    else:
        history += [list(memblocks)]
