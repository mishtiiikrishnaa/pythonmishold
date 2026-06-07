#program 48, page 157, question bank
number=int(input(" a number "))
numm=number
summ=0
while number!=0:
    dig=number%10
    number=number//10
    summ=summ+dig
print("the sum of digits of", numm, "is ", summ)

    
