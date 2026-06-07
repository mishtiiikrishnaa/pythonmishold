num=11
summ=0
while num>0:
    r=num%10
    for p in range(2):
        po=r*2**p
        summ=summ+po
    num=num//10
print(summ)

