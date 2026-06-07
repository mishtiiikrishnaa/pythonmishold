#perfect number
p=int(input("give a number: "))
s=0
for i in range(1,p):
    if p%i==0:
        s+=i
if s==p:
    print("perfect")
else:
    print("not perfect")
