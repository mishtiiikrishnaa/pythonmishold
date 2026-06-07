numbers=[2,4,8,10]
ptr=numbers
for c in range(0,3):
    print(ptr[c], "@", end= " ")
for c in range(0,4):
    ptr[c]*=2
print()
for c in range(0,4):
    print(numbers[c], "#", end= " ")