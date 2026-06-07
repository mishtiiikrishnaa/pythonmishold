m=int(input("a range: "))
tot=5
print(tot)
for n in range(2,m+1):
    if n%2==0:
        tot=tot*2
    else:
        tot=tot+2
    print(tot)
