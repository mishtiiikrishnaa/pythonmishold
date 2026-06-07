#page 370, q(4)
lyst=eval(input("enter list with numbers from 1 to 12: "))
for number in range(len(lyst)):
    if lyst[number]>10:
        lyst[number]=10
print(lyst)
