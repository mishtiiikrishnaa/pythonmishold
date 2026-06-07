tp=eval(input("enter a tuple of numbers: "))
ls=list(tp)
for i in range(len(ls)):
    for j in range(len(ls)-i-1):
        if ls[j]>ls[j+1]:
            ls[j],ls[j+1]=ls[j+1],ls[j]
print("smallest no.:", ls[-1])
print("largest no.:", ls[0])
