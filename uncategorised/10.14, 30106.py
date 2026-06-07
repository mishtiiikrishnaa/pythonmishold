#pg 353, 10.14
lyst=eval(input("number list of 4 no.s: "))
a=lyst[0]
b=lyst[1]
c=lyst[2]
d=lyst[3]
if a>b and a>c and a>d:
    greatest=a
elif b>a and b>c and b>d:
    greatest=b
elif c>a and c>b and c>d:
    greatest=c
elif d>a and d>b and d>c:
    greatest=d
if greatest <= len(lyst)/2:
    print("max. element,", greatest, ", lies in the 1st half of", lyst)
else:
    print("max. element,", greatest, ", lies in the 2nd half of", lyst)
