def fib(a):
    f,s=-1,1
    print(f+s,end= " ")
    for i in range(a):
        t=f+s
        f,s=s,t
        print( f+s, end= " ")
n=int(input("some range: "))
fib(n)
