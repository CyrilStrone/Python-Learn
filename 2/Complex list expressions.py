print([(x,y) for x in [1,2,3] for y in [1,2,3] if x!=y])

combs = []
for x in [1,2,3]:
    for y in [1,4,3]:
        if x!=y:
            combs.append((x,y))

print (combs)