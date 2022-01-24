from functools import reduce
reduce((lambda x,y:x+y),[1,2,3,4]) #20
reduce((lambda x, y:x*y),[1,2,3,4]) #24

from functools import reduce
items = [11,2,-7,14,3,62,1]
_max = reduce(lambda a,b:a if (a>b) else b,items)

print(_max)  #62