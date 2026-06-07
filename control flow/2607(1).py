#checking whether given no. is armstrong number or not
gn=123
d1=gn%100
print(d1)
d2=d1//10
print(d2)
d3=d2//2
print(d3)
d4=d1%20
print(d4)
if d2**3+d3**3+d4**3==gn:
    print("given number is armstrong no.")
else:
    print(d2**3,"+",d3**3,"+",d4**3,"=",d2**3+d3**3+d4**3)

total=0
num=int(input("number: " ))
num=sum1
while num>0:
    r=num%10
    total=total+(r**3)
    num=num//10
print(total)
if total==sum1:
    print("given is armstrong")
else:
    print("given isnt armstrong")



