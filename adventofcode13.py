import operator


with open("advent13big.txt") as f:
    lines = [i.strip() for i in f.readlines()]

fw = {}

for line in lines:
    line = [i.replace(":", "") for i in line.split()]
    if int(line[0]) not in fw:
        # FW [DEPTH, CUR, DIRECTION]
        fw[int(line[0])] = [int(line[1]),0,operator.add]

#print(fw)

caught = []
for iteration in range(max(fw.keys()) + 1 ):
    print ("===============iteration %s" % iteration )
    if iteration in fw and fw[iteration][1]==0:
	   print("caught")
	   caught.append([iteration, fw[iteration][0]])
    for level, values in fw.items():
	   values[1] = values[2](values[1],1)
	if values[1] == 0:
	    values[2] = operator.add
	elif  values[1] == values[0] - 1:
	    values[2] = operator.sub
	#print(fw)
    #print(caught)
result = 0
l = [level * depth for level, depth in caught]
for i in l:
    result += i
print(result)
