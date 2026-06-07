#page 400[13]
m=[]
tup=eval(input("enter a tuple: "))
lst=list(tup)
lst.sort()
for i in lst:
    m.append([lst.count(i),i])
m.sort()
mode=m[-1][1]
print("mode = ",mode)


