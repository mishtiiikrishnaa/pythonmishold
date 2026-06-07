n=int(input("range: "))
for c in range(n):
    for r in range(1,c+1):
        print(chr(65+r), end= " ")
    print()