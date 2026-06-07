n=int(input("number of rows: "))
for i in range(n):
    for j in range(0,i):
        print(chr(65+j),end= "")
    print()
    
