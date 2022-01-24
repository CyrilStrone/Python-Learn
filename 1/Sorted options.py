def get_second(x):
    return x[1]

l = [['a',2],['c',1],['b',7]]
print(sorted(l))
print(sorted(l, key=get_second))