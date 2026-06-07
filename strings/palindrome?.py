num=int(input("number: "))
che=num
sim=0
while num!=0:
    sim=sim*10+(num%10)
    num=num//10
if che==sim:
    print("palindrome")
else:
    print("no")