n=int(input("number: "))
r=n
tot=0
while n!=0:
    tot=tot+(n%10)**3
    n=n//10
if r==tot:
    print("armstrong no")
else:
    print("not an armstrong no")