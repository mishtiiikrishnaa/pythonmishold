#fibonacci series
r=int(input("range: "))
f,s=-1,1
print(f+s,end= " ")
for i in range(r):
    t=f+s
    f,s=s,t
    print(f+s,end= " ")
