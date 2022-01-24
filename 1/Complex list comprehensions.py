print([(x,y) for x in [1,2,3] for y in [1,4,3] if x!=y])

combs = []
for x in [1,2,3]:
    for y in [1,4,3]:
        if x!=y:
            combs.append((x,y))
            
print(combs)

matrix = [[1,3,4,6],[6,3,2,8],[10,1,1,4]]

print([[row[i] for row in matrix] for i in range(4)])