#sum of digits
n=input("enter a number: ")
s=0
for i in n:
    s+=int(i)
print(s)

n1=int(input("enter a number: "))
s=0
while n1!=0:
    d=n1%10
    s=s+d
    n1=n1//10
print(s)
