lyst=eval(input("a number list: "))
lystodd=[]
lysteven=[]
for element in lyst:
    if int(element)%2==0:
        lysteven.append(element)
    else:
        lystodd.append(element)
print("odd numbers: ", lystodd)
print("even numbers: ", lysteven)