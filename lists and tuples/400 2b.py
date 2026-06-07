#page 400[2][b]
req=[]
terms=10
fir=-1
sec=1
thr=fir+sec
req.append(0)
for ter in range (0,terms-1):
    fir,sec=sec,thr
    thr,sec=fir,sec
    thr=sec+thr
    req.append(thr)
ft=int(input("a fibonacci number: "))
if ft in req:
          print(ft, "is the",(req.index(ft))+1,"th/rd/nd term of the fibonacci series")
