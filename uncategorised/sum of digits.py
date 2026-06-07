num=int(input("number: "))
sim=0
while num!=0:
    sim=sim+(num%10)
    num=num//10
print(sim)