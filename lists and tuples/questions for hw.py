#WAP to read a list of no.s, square the no.s in odd index postions, and cube the no.s in even index positions
#WAP to read two lists of the same size, generate a new list which contains
#the sum of elements of first list and second list.

lyst=eval(input("list: "))
for num in lyst[1::2]:
    num=num**2
    print(num)
for number in lyst[0::2]:
    number=number**3
    print(number)
