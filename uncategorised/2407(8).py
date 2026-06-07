rows = 6
for columns in range(0, rows):
    for no_of_stars in range(0, columns + 1):
        print(" * ", end=' ')
    print(" ")
for columns in range(rows, 0, -1):
    for no_of_stars in range(0, columns - 1):
        print(" * ", end=' ')
    print(" ")
