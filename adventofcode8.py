

#b inc 5 if a > 1
#a inc 1 if b < 5
#c dec -10 if a >= 1
#c inc -20 if c == 10

import os
import operator
import re
ops = { "inc": operator.add, "dec": operator.sub, ">": operator.gt, "<": operator.lt, ">=": operator.ge, "<=": operator.le, "==": operator.eq, "!=": operator.ne}

with open("advent8big.txt") as f:
    lines = [i.strip() for i in f.readlines()]

print(lines)
registers={}

maxi = 0
for line in lines:
    line = line.split()
    print(line)
    if line[0] not in registers:
        registers[line[0]]=0
    if line[4] not in registers:
        registers[line[4]]=0

    if ops[line[5]](registers[line[4]], int(line[6])):
        print("yes")
        registers[line[0]] = ops[line[1]](registers[line[0]], int(line[2]))

    print(registers)
    if max(registers.values()) > maxi:
        maxi = max(registers.values())
print(max(zip(registers.values(), registers.keys())))
print(maxi)
