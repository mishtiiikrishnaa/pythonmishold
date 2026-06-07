#function w/ argument but no return
def fact(n):
         j=1
         for i in range(1,n+1):
                  j*=i
         print(j)
def palindrome(a):
         if a[::-1]==a:
                  print(a,"is palindrome")
         else:
                  print(a,"is not palindrome")
def sumofdigits(k):
         k1=str(k)
         s=0
         for o in k1:
                  s=s+int(o)
         print("sum of digits:",s)
choice=int(input("1,2,3? /n 1. factorial 2. palindrome 3. sum of digits of number : "))
if choice==1:
         n=int(input("enter a number: "))
         fact(n)
elif choice==2:
         a=input("enter a string: ")
         palindrome(a)
elif choice==3:
         k=int(input("enter a number: "))
         sumofdigits(k)
else:
         print("enter a valid number!")
         
