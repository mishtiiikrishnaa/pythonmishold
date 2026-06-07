#sum of numbers
number=int(input("give a number: "))
totalsum=0
result=number
while number>0:
    indidigit=number%10
    totalsum=totalsum+(indidigit**3)
    number=number//10
if totalsum==result:
    print(result, "is an armstrong number")
else:
    print(result, "isn't an armstrong number")

