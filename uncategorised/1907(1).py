total=0
num=int(input("number: " ))
while num>0:
    r=num%10
    total=total+r
    num=num//10
    print(num)
print(total)
