rows=5
columns=rows
while columns>=1:
    no_of_spaces=rows
    while no_of_spaces>columns:
        print( "  " , end=" ")
        no_of_spaces-=1
    no_of_stars=1
    while no_of_stars<=columns:
        print(" *", end=" ")
        no_of_stars+=1
    print()
    columns-=1
    
