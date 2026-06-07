gt=((2,5),(4,2),(9,8),(12,10))
ce=0
ggt=list(gt)
for el in range(len(gt)):
    for e in ggt[el]:
        lt=list(ggt[el])
        for l in lt:
            if l%2==0:
                pass
            elif l%2!=0:
                break
    ce+=1
print(ce)
