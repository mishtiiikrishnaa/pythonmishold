#page 382, 11.10
tup=eval(input("four element tuple: "))
a,b,c,d=tup
print("tuple unpacked in:",a,b,c,d)
tup=c,d,a,b
print("tuple after swapping elements:",tup)
