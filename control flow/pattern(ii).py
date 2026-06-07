n = 1
ran=int(input("enter a range: "))
for i in range(ran):
    # Inner loop for each row
    for j in range(i + 1):
        print(n, end=" ")
        n += 1  # Increment 'n' for the next value
    print()  # Move to the next line after each row
