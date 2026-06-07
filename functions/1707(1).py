#fibonacci sequence
m=-1
n=1
o=m+n
p=0
q=int(input("no.of terms: "))
while p<=q:
    m,n=n,o
    n,o=o,m
    print(p)
