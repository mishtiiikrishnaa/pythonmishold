m=int(input("enter a number: "))
s=0
n=m
while m>0:
         r=m%10
         s+=r**3
         m=m//10
if s==n:
         print(n,"is an armstrong number")
else:
         print(n,"is not an armstrong number")
         
