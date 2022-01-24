def func(a,b,c=2):
    return a+b+c

func(1, 2)# a = 1, b = 2, c = 2
func(1, 2, 3) # a = 1, b = 2, c = 3
func(a=1, b=3) # a = 1, b = 3, c = 2
func(a=3, c=6) # a = 3, c = 6, b is undefined