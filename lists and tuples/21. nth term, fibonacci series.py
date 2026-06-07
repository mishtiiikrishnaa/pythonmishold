fib=[]
terms=int(input("number of terms: "))
fir=-1
sec=1
thr=fir+sec
for ter in range (0,terms-1):
    fir,sec=sec,thr
    thr,sec=fir,sec
    thr=sec+thr
    fib.append(thr)
n=int(input("nth term? "))
print(fib[n])

