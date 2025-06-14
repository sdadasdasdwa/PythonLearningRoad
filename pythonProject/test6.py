dicc={}
with open('ratings.dat','r') as f:
    for i in range(3):
        line = f.readline().strip().split("::")
        print((line))
        if line[0] not in dicc.keys():
            dicc[line[0]]=set()
        dicc[line[0]].add((line[3]))
print(dicc)
