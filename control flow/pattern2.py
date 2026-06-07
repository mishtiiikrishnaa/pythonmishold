n=int(input("range: "))
for c in range(n,0,-1):
    for r in range(c,0,-1):
        print("*", end= " ")
    print()