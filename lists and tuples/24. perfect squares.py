R1=int(input("enter start: "))
R2=int(input("enter end: "))
lyst=[]
for num in range(R1, R2+1):
    sq=num*num
    summ=0
    n=sq
    while sq>0:
        summ=summ+sq%10
        sq=sq//10
    if summ<=10:
        lyst.append(n)
    if n>=R2:
        break
print(lyst)