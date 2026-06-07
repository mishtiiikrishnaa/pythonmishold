terms=int(input("number of terms: "))
fir=-1
sec=1
thr=fir+sec
print(thr, end=" ")
for ter in range (0,terms-1):
    fir,sec=sec,thr
    thr,sec=fir,sec
    thr=sec+thr
    print(thr, end=" ")
print()