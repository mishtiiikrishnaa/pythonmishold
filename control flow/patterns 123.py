r=1
n=int(input("number of rows: "))
for i in range(n):
    for j in range(0,i+1):
        print(r,end= "")
        r+=1
    print()
    
