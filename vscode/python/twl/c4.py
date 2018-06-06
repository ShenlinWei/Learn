import time
def decotator(func):
    def wrapper():
        print(time.time())   
        func ()
    return wrapper

@decotator
def f1():
    print('This is a function')


f1()