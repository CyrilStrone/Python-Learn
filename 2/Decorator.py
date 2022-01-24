def decorator_name(func):
    def decorator_fn(*args,**kwargs):
        print("Something is happening before the function is called.") 
        func()
        print("Something is happening after the function is called.") 
        return
    decorator_fn

def say_hello():print("Hello")

say_hello = decorator_name(say_hello)
say_hello()


def say_hello():
    print("Hello!")
say_hello()