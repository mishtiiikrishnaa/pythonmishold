x=int(input("enter a value for the numerator: "))
y=int(input("enter a value for the denominator: "))
n=int(input("enter a limit for exponents to be used: "))
r=int(input("enter a range of terms: "))
for no in range(1,r+1):
    term=x**n/y**n
    n=n+1
    print(term)
    
