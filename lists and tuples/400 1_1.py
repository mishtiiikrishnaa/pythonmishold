#page 400[1]
req=[]
terms=9
fir=-1
sec=1
thr=fir+sec
for ter in range (0,terms-1):
    fir,sec=sec,thr
    thr,sec=fir,sec
    thr=sec+thr
    req.append(thr)
print(tuple(req))
