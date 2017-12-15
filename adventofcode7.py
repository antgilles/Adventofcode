import os
import re
import sys

with open('advent7big.txt') as f:
    programlines = [i.strip() for i in f.readlines()]

node = 'cyrupz'
#node = 'tknk'
#print(programlines)
prog =  {}

for i in programlines:
    m = re.match(r"(\w+)\s+\((\w+)\)", i)
    progname=m.groups()[0]
    prog[m.groups()[0]]= [m.groups()[1]]

    #    prog[i[0]]= [i[1]]
    m = re.match(r".*-> (.*)", i)
    if m:
        child = []
        for elem in [i.split(', ') for i in m.groups()]:
            child += elem
        prog[progname].append(child)
#print(prog)


def getweight(n):
    #print(prog[n])
    global tomodify

    if  len(prog[n]) == 1:
        #print("ENFANT")
        return int(prog[n][0])
    else:
        childcomp = {}
        #print(prog[n][1])
        total = 0
        for child in prog[n][1]:
            childweight = getweight(child)
            #print('%s %s' % (child,childweight))
            total += childweight
            if childweight not in childcomp:
                childcomp[childweight]=[]
            childcomp[childweight].append(child)

        if not tomodify:
            #print(childcomp)
            if len(childcomp) > 1:
                for key,value in childcomp.items():
                    #print('%s:%s' % (key,value))
                    if len(value) == 1:
                        print('remplacer %s de %s' % (key,value[0]))
                        valueorig = key
                        nodetoreplace = value[0]
                    else:
                        print ('remplacer par %s' % key)
                        valuedest = key
                tomodify = [nodetoreplace, valuedest]
        else:
            return 0

        return(total + int(prog[n][0]))


tomodify = 0
getweight(node)
print(tomodify)

print(prog[tomodify[0]])
