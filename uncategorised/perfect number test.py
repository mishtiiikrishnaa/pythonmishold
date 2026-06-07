#perfect?
numr=int(input("enter a number:"))
totes=0
for fact in range(1, numr):
    if numr%fact==0:
        totes=totes+fact
if numr==totes:
    print(numr,"is perfect")
else:
    print(numr,"is imperfect")
