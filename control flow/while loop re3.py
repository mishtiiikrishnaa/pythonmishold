i=1
while i<=5:
    j=1
    while j<=i:
        print("&", end= " ")
        j+=1
    print(" ")
    i+=1

for i in [1, 2, 3, 4, 5]:
    for j in range(i):
        print("&"*j)


