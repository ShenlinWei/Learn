from functools import reduce

list_x=[1,2,3,4,5,6,7,8]
list_y=[1,2,3,4,5,6]

r=reduce(lambda x,y: x+y,list_x)

print(type(r))
print(r)