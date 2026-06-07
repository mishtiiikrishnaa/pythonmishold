#sum of numbers
number=int(input("give a number: "))
ts=0
while number>0:
    r=number%10
    ts+=r
    number=number//10
print(ts)
