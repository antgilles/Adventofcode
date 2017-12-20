from  adventofcode10_2 import gethash

res = 0
phrase = 'jzgqcdpd'
for i in range(128):
    h = gethash(phrase + '-' + str(i))
    line = "{0:8b}".format(int(h,16))
    res += line.count('1')

print(res)
