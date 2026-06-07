# WAP to read a list and slice it into two halves.
# |^ find max of sublist 1 and find min of sublist 2 without max() and min()
lyst = eval(input("enter a number list: "))
sublyst1 = []
sublyst2 = []
lent = int(len(lyst) / 2)
for num in range(0, lent):
    sublyst1.append(lyst[num])
for i in range(1, len(sublyst1) - 1):
    for j in range(0, len(sublyst1) - 1):
        if sublyst1[j] > sublyst1[j + 1]:
            sublyst1[j], sublyst1[j + 1] = sublyst1[j + 1], sublyst1[j]
print("greatest in first half: ", sublyst1[-1])
for number in range(lent, len(lyst)):
    sublyst2.append(lyst[number])
for I in range(1, len(sublyst2)):
    for J in range(0, len(sublyst2) - 1):
        if sublyst2[J] > sublyst2[J + 1]:
            sublyst2[J], sublyst2[J + 1] = sublyst2[J + 1], sublyst2[J]
print("least in second half: ", sublyst2[0])
