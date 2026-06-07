range1=int(input("some number: "))
for r in range(range1):
    for j in range(r):
        print(chr(65+j), end=" ")
    print()