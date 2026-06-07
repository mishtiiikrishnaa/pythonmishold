#typeC [1]
tup=[]
fir=-1
sec=1
thr=fir+sec
for ter in range (0,10):
    fir,sec=sec,thr
    thr,sec=fir,sec
    thr=sec+thr
    tup.append(thr)
print(tuple(tup))

