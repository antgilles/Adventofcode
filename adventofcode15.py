

#genstart = (65,8921)
genstart = (873,583)
factor = (16807, 48271)
dividevalue = 2147483647

res = 0
for iteration in range(40000000):
    gen = [genstart[i] * factor[i] % dividevalue for i in range(2)]

    if iteration % 100000 == 0: print(iteration)
    if list("{:032b}".format(int(gen[0])))[-16:] == list("{:032b}".format(int(gen[1])))[-16:]:
        res += 1
    genstart = gen

print(res)
