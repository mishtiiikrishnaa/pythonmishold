n=int(input(" a number: "))
sum=0
while(n!=0):
    sum=sum+n%10
    n=n//10
print(sum)
print("\n")
n=int(input(" a number: "))
sn=str(n)
sum=0
for i in sn:
    if (n!=0):
        sum=sum+n%10
        n=n//10
    else:
        break
print(sum)