def p(d):
    l=[]
    for i in d:
        if d[i][2]>500:
            k=d[i]
            o=k[0:2]
            l.append(o)
    print(l)
b={}
while True:
    bid=input("book id: ")
    bn=input("book name: ")
    ba=input("book author: ")
    bp=int(input("book price: "))
    b[bid]=[bn,ba,bp]
    c=input("more? y/n: ")
    if c=="y":
        ch=True
    else:
        p(b)

