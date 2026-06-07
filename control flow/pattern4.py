n=int(input("range: "))
for c in range(n):
    for s in range(1,n-c):
        print(" ", end= " ")
    for r in range(1,c+1):
        print(c,end= " ")
    print(" ")
