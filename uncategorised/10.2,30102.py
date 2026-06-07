#pg 334, 10.2
lyst=eval(input("list of numbers, total >20."))
print("slice 1: ", end= " ")
for char in lyst[5:15:2]:
    print(char, end= ",")
sim=0
for num in lyst[5:15:2]:
    sim=sim+num
print(" ")
print("sum: ", sim)
print("slice 2: ", end= " ")
for chart in lyst[::4]:
    print(chart, end= ",")
print(" ")
suma=0
for numb in lyst[::4]:
    suma=suma+numb
print("average: ", suma/(len(lyst[::4])))

    
