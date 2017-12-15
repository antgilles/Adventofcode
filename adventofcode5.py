import os

with open('input5.txt') as f:
    passlist = f.readlines()

passlist = [int(i.strip()) for i in passlist]

print(passlist)

#passlist =  [0,3,0,1,-3]
result = 0
cur = 0

def getnext(cur):
  nextval = cur + passlist[cur]
  if passlist[cur] >= 3:
      passlist[cur] -= 1
  else:
      passlist[cur] += 1
  return nextval

while 1:
  #print(cur)
  cur = getnext(cur)
  result += 1
  if cur < 0 or cur == len(passlist):
    break

print("RESULT : " + str(result))
