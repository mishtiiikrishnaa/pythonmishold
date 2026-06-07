#read name and 3 subject marks of 5 students, in tuples. ask user for name.
#for entered name, increase 2nd subject marks by 5%, print updated tuple.
L=[]
for n in range(5):
    name=input("enter name: ")
    marks=eval(input("enter marks of 3 subjects in tuple: "))
    L.extend([name,marks])
print(L)
nwme=input("enter name: ")
if nwme in L:
    i=L.index(nwme)
    I=i+1
    J=list(L[I])
    J[1]=J[1]+(0.05*J[1])
    K=tuple(J)
    print(L)
else:
    print("name not found")
