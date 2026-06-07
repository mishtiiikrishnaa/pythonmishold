m=int(input("enter a number: "))
n=0
for i in range(1,m):
         if m%i==0:
                  n+=i
if n==m:
         print(m,"is a perfect number")
else:
         print(m,"is not a perfect number")
