rows=int(input("enter the number of rows required: "))
for columns in range(rows+1,0,-1):
    for no_of_stars in range(0,columns-1):
        print(" * ", end=" ")
    print(" ") 
