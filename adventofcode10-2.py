import functools

def getinput(s):
    length = [ord(i) for i in phrase] + [17, 31, 73, 47, 23]
    return length

def getdensehash(l):
    ret = []
    for i in range(16):
        ret.append(functools.reduce(lambda i, j: int(i) ^ int(j), l[(i * 16):(i * 16) + 16]))
    return ret

def gethash(s):
    l = getinput(s)
    liste = [i for i in range(256)]
    pos = 0
    skip = 0
    for iteration in range(64):
        for i in l:
            posend = (pos  + i )
            if posend > len(liste):
                posend = posend % len(liste)
                rep = list(liste[pos:]) + list(liste[:posend])
            else:
                rep = list(liste[pos:posend])
            rep.reverse()
            for j in range(len(rep)):
                liste[(pos % len(liste)+ j) % len(liste)] = rep[j]
            pos = (pos + i + skip) % len(liste)
            skip += 1
    densehash = getdensehash(liste)
    h = ''.join(['{:02x}'.format(i) for i in densehash])
    return h

phrase = '225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110'
phrase = '1,2,3'
#phrase = 'flqrgnkx-0'

print(gethash(phrase))
