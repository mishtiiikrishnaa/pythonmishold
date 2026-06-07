def series(a,l):
    d=(l-a)/3
    return a, a+d, a+(2*d), a+(3*d)
n1=int(input("n1: "))
n2=int(input("n2 :"))
print(series(n1,n2))
        
