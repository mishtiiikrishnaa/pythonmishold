d1=eval(input("a dictionary: "))
D1={}
D=list(d1.values())
for i in D:
    D1[i]=D.count(i)
for j in D1:
    if D1[j]>1:
        print(D1[j], "keys have the same value")