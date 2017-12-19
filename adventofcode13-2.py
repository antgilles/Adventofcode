import operator
import copy
import sys



with open("advent13big.txt") as f:
    lines = [i.strip() for i in f.readlines()]

fw = {}

for line in lines:
    line = [i.replace(":", "") for i in line.split()]
    if int(line[0]) not in fw:
        # FW [DEPTH, CUR, DIRECTION]
        fw[int(line[0])] = int(line[1])

for delay in range(10000000):
    if delay % 1000 == 0:
        print(delay)
    caught = 0
    for iteration in range(delay, max(fw.keys()) + 1 + delay):
        pos = iteration - delay
        #print ("===============iteration %s" % iteration )
        if pos in fw and (iteration % (fw[pos] * 2 - 2)) == 0:
            #print("caught")
            caught = 1

    if caught == 0:
       print(delay)
       break
