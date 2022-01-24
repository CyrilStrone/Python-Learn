from audioop import reverse
from operator import le


l=[['a,2'],['c',1],['b',7]]
print(sorted(l))
print(sorted(l, key=lambda x:x[1]))
print(sorted(l, key=lambda x:x[1],reverse=True))
d={'a':1,'b':7,'c':5}
for k,v in sorted(d.items(), key = lambda x: x[1]):print (k,v)