print("printing equilateral triangle pyramid using * symbol")
# printing full Triangle pyramid using stars
length = 7
m = (2 * length) - 2
for columns in range(0, length):
    for no_of_stars in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for no_of_stars in range(0, columns + 1):
        print("* ", end=" ")
    print(" ")
