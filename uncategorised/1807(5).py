times=10
for n in range(1,times):
    o=1
    for p in range(times,0,-1):
        if p>1:
            print(" ", end=" ")
        else:
            print(o, end=" ")
            o+=1
    print( )
