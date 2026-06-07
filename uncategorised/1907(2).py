total=0
num=int(input("number: " ))
while num>0:
    r=num%10
    total=total*10+r
    num=num//10
    print(total)
print(total)


