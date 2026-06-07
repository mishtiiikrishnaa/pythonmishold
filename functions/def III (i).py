#function w/out argument but w/ return
def fact():
         n=int(input("number: "))
         j=1
         for i in range(1,n+1):
                  j*=i
         return j
def palindrome():
         a=input("string: ")
         if a[::-1]==a:
                  return a,"is palindrome"
         else:
                  return a,"is not palindrome"
def sumofdigits():
         k=int(input("number: "))
         k1=str(k)
         s=0
         for o in k1:
                  s=s+int(o)
         return s
choice=int(input("1,2,3? /n 1. factorial 2. palindrome 3. sum of digits of number : "))
if choice==1:
         print(fact())
elif choice==2:
         print(palindrome())
elif choice==3:
         print(sumofdigits())
else:
         print("enter a valid number!")
         
