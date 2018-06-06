list_x = [1,2,3,4,5]

def squre(x):
    return x*x

list_y = map(squre,list_x)
print(list(list_y))