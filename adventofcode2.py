import sys

with open('input2.txt') as f:
    content = f.readlines()

ret = 0
for i in content:
    j = i.strip().split('\t')
    jlist = [int(k) for k in j]
    for x in range(len(jlist)):
        for y in range(len(jlist)):
            if (x != y) and (jlist[x] % jlist[y] == 0):
                ret += jlist[x] / jlist[y]
print (ret)
