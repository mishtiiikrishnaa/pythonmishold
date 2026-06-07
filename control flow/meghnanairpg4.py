k=int(input("enter a number: "))
n=0
s=k
while k>0:
         r=k%10
         n=n*10+r
         k=k//10
if s==n:
         print(s,"is a palindrome number")
else:
         print(s,"is not a palindrome number")
