#armstrong
n=input("enter a number: ")
s=0
for i in n:
    s=s+(int(i)**3)
if s==int(n):
    print("armstrong")
else:
    print("not armstrong")
