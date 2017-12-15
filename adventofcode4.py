import os

with open('input4.txt') as f:
    passlist = f.readlines()
result = 0
for password in passlist:
    ko = 0
    wordlist = password.strip().split()
    print(wordlist)
    for w in wordlist:
        tempwordlist = list(wordlist)
        #if wordlist.count(w) > 1:
        #    print("KO : %s" % w)
        #    ko = 1
        #    break
        tempwordlist.remove(w)
        #print(tempwordlist)
        for tempword in tempwordlist:
            tmptmp = list(tempword)
            if len(tmptmp) != len(w):
                break
            else:
                print("%s vs %s" %  (tmptmp, w))
                for letter in w:
                    if letter in tmptmp:
                        tmptmp.remove(letter)
                    else:
                        print('not palyn')
                        break
                print (len(tmptmp))
                if len(tmptmp) == 0:
                    ko = 1
    if not ko:
        print("==== ok")
        result += 1
    else:
        print ("---- ko")

print(result)
