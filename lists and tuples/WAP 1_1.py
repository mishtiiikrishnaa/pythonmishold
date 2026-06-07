#WAP to read a list of no.s, square the no.s in odd index postions, and cube the no.s in even index positions
lyst=eval(input("list: "))
for num in range(1,len(lyst),2):
    lyst[num]=lyst[num]**2
for number in range(0,len(lyst),2):
    lyst[number]=lyst[number]**3
print(lyst)

