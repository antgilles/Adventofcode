with open("advent12big.txt") as f:
    lines = [i.strip() for i in f.readlines()]

graph = {}

for line in lines:
    line = [i.replace(",", "") for i in line.split()]
    if line[0] not in graph:
        graph[line[0]] = line[2:]

#print(graph)
visited=[]

def parseGraph(node):
    visited.append(node)
    for child in graph[node]:
        if child not in visited:
            parseGraph(child)

parseGraph('0')
result=0
for node in graph.keys():
    if node in visited:
        result +=1
print(result)
