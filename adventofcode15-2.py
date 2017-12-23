

#genstart = (65,8921)
genstart = (873,583)


def findnextvalue(start, AorB):
    factor = (16807, 48271)
    multiple = (4,8)
    dividevalue = 2147483647
    ret = 1
    while ret % multiple[AorB] != 0:
        ret = start * factor[AorB] % dividevalue
        start = ret
    return ret

res = 0
for iteration in range(5000000):
    gen = [findnextvalue(genstart[i], i) for i in range(2)]

    if iteration % 100000 == 0: print(iteration)
    if list("{:032b}".format(int(gen[0])))[-16:] == list("{:032b}".format(int(gen[1])))[-16:]:
        res += 1
    genstart = gen

print(res)
