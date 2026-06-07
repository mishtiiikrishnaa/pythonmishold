x=3
n=int(input("power range of choice: "))
s=x
sign=+1
for a in range(1,n+1):
    f=1
    for i in range(1,a+1):
        f=f*i
    term=((x**a)*sign)/f
    s=s+term
    sign=sign*-1
print("sum=",s)
