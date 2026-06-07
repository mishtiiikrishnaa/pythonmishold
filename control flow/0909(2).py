#print some pattern, 9 sept(2)
number=int(input("enter a number: " ))
product=1
while number>0:
    digit=number%10
    product=product*digit
    number=number//10
print(product)
