#page 335, making true copy of list
a=[1,2,3]
b=a
a[1]=5
print(a,b)
a=[1,2,3]
b=list(a)
a[1]=5
print(a,b)
