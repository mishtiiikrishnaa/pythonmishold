L=eval(input("give a list of numbers: "))
L1=L[:]
for n in range(0,len(L)):
    if n%2==0:
        L[n]=(L[n]+1)
    elif n%2!=0:
        L[n]=(L[n]-1)
print("new list: ", L)
