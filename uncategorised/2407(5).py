rows=int(input("enter no. of rows wanted: "))
k=2*rows-2
for columns in range(rows,-1,-1):
    for no_of_stars in range(k,0,-1):
        print(end=" ")
    k+=1
    for no_of_stars in range(0,columns+1):
        print("*", end=" ")
    print(" ")
    
