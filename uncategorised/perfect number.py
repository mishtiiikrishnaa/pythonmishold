numr=int(input("a number: "))
totes=0
for fact in range(1, numr):
    if numr%fact==0:
        totes+=fact
if totes==numr:
    print(numr, "is perfect")
else:
    print(numr, "isn't perfect")

