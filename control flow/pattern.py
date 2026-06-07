no=int(input("no. of rows: "))
for ro in range(0, no+1):
    for mo in range(0,ro):
        print(chr (65+mo), end= " ")
    print()