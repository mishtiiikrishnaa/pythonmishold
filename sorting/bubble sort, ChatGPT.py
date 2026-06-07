N=eval(input("enter a list of numbers: "))
for i in range(1,len(N)-1):
    for j in range(0,len(N)-1):
        if N[j]>N[j+1]:
            N[j],N[j+1]=N[j+1],N[j]
print(N)




