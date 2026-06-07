#WAP to read a list of numbers. every odd index to be multiplied by 5 and every even index to be divided by 2.
#print the new list, slice the list obtained in which every 3rd element of is taken out, and find its sum and
#average of sliced list.
lyst=eval(input("a list of numbers: "))
for number in range(1,len(lyst),2):
    lyst[number]*=5
for num in range(0,len(lyst),2):
    lyst[num]/=2
print(lyst)
slicedlyst=[]
sim=0
for element in range(2,len(lyst),3):
    sim+=lyst[element]
print(lyst[2::3])
print("sum: ", sim)
print("average: ", sim/len(lyst[2::3]))
