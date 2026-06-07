total=0
num=int(input("number: " ))
v=int(input("same number: "))
num=v
while num>0:
    r=num%10
    total=total+(r**3)
    num=num//10
print(total)
if total==v:
    print("given is armstrong")
else:
    print("given isnt armstrong")
