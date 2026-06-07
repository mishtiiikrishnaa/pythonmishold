#1. WAP to read a list and print only the prime numbers in the list.
lyst=eval(input("enter a number list: "))
pno=[]
for no in lyst:
    if (no==2 or no==3 or no==5) and no!=1:
        pno.append(no)
    elif (no%2!=0 and no%3!=0 and no%5!=0) and no!=1:
        pno.append(no)
print("prime numbers in list: ",pno)

