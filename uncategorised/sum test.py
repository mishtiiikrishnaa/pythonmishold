#sum of the digits of a number
num=int(input("enter a number: "))
strnum=str(num)
tot=0
for ch in strnum:
    tot+=int(ch)
print(tot)
