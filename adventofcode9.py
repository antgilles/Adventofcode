
with open("advent9big.txt") as f:
    lines = [i.strip() for i in f.readlines()]
score = 0
for line in lines:
    level = 0

    ingarbage = 0
    print(line)
    line = list(line)
    while line:
        char = line.pop(0)
        print(char)
        #if char == '{' and ingarbage == 0:
        #    level += 1
            #score += level
        #elif char == '}' and ingarbage == 0:
        #    level -= 1
        #elif char == '<' and ingarbage == 0:
        #    ingarbage = 1
        #elif char == '>':
        #    ingarbage = 0
        #elif char == '!' and ingarbage == 1:
            #print('POP')
        #    line.pop(0)

        if char == '<' and ingarbage == 0:
            ingarbage = 1
        elif char == '>':
            ingarbage = 0
        elif char == '!' and ingarbage == 1:
            #print('POP')
            line.pop(0)
        elif ingarbage == 1:
            score += 1
print(score)
