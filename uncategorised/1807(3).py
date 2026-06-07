times=int(input("enter no of rows: "))
termnum=1
while termnum<=times:
    valueofterm=1
    while valueofterm<=termnum:
        print ((termnum*2-1), end=" ")
        valueofterm=valueofterm+1
    termnum=termnum+1
    print()
