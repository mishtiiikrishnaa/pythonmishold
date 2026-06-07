L=eval(input("enter a number list: "))
for num in range(1,len(L),2):
    L[num]-=1
for numb in range(0,len(L),2):
    L[numb]+=1
print(L)
