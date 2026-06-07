NUMBER=1
RANGE=int(input("give a range: "))
STOP=1
for i in range(RANGE):
    for j in range(1,STOP):
        print(NUMBER, end=" ")
        NUMBER+=1
    print(" ")
    STOP+=1

