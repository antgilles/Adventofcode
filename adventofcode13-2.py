import operator
import copy


with open("advent13big.txt") as f:
    lines = [i.strip() for i in f.readlines()]

fwinit = {}

for line in lines:
    line = [i.replace(":", "") for i in line.split()]
    if int(line[0]) not in fwinit:
        # FW [DEPTH, CUR, DIRECTION]
        fwinit[int(line[0])] = [int(line[1]),0,operator.add]

#print(fw)


for delay in range(10000):
	print('#### DELAY = %s' % delay)
	fw = copy.deepcopy(fwinit)
	#print fw
	caught=0
	for iteration in range(max(fw.keys()) + delay + 1 ):
	    #print ("===============iteration %s" % iteration )
	    #print("pos : %s" % str(iteration - delay))
	    if iteration - delay in fw and fw[iteration - delay][1]==0:
		print("caught")
		caught=1
		break
	    for level, values in fw.items():
		values[1] = values[2](values[1],1)
		if values[1] == 0:
		    values[2] = operator.add
		elif  values[1] == values[0] - 1:
		    values[2] = operator.sub
#		print(fw)
#	    print(caught)
	if not caught:
		print(delay) 
	   	break 
