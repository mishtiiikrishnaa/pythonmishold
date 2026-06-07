m=int(input("give a number: "))
s=0
for d in range(1,m):
    if m%d==0:
        f=d
        s=s+f
if s==m:
    print("the given no is perfect :)")
else:
    print("the given no is imperfect :(")
