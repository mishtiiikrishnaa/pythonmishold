times=int(input("enter no of rows: "))
for n in range(0,times+1):
    for o in range(times-n,0,-1):
        print (o, end=" ")
    print( )
