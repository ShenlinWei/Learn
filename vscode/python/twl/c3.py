import time
def decotator(func):
    def wrapper():
        print(time.time())   
        func ()
    return wrapper

def f1():
    print('This is a function')


f=decotator(f1)
f()