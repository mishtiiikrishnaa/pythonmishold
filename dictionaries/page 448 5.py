l={}
while True:
    p=input("enter product name: ")
    pr=int(input("price: "))
    l[p]=pr
    ch=input("enter more products? y/n ")
    if ch=="y":
        ch=True
    else:
        break
P=input("product name?:")
print(l.get(P,"not purchased yet"))