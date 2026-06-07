for n in range(100,1001):
    r=n
    tot=0
    while n!=0:
        tot=tot+(n%10)**3
        n=n//10
    if r==tot:
        print(r)
    else:
        pass