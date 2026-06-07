#reverse a number
n=input("enter a number: ")
print(n[::-1])

n1=int(input("enter a number: "))
s=0
while n1!=0:
    d=n1%10
    s=s*10+d
    n1=n1//10
print(s)
    
