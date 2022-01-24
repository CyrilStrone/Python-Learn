from re import X


x = 88 #Global x

def func():
    global X
    X = 99 #Global X:outside def

func()
print(x)#99