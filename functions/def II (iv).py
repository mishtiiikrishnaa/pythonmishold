#function w/argument but no return
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
fact(5) #function call 1
x=4     #function call 2
fact(x)
y=int(input('n:')) #function call 3
fact(y)
