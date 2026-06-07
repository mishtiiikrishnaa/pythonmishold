#create a dictionary with book id, stock, qty sold for 5 items. get bookid
#from user and retrieve the qty sold.
#assume cost of qty is 100/item. print the total amt for products sold along with product name.
#(pt2) based on book name that ends with letter e,
#increase stock by 5%. update new stock into dictionary.

d,dh={},{}
L,Lh=[],[]
for i in range(5):
    bid=int(input("book id: "))
    bn=input("book name: ")
    stk=int(input("stock: "))
    qty=int(input("qty sold: "))
    d["book id"]=bid
    d["stock"]=stk
    d["qty sold"]=qty
    dh["book name"]=bn
    dh["book id"]=bid
    Lh.append(dh)
    print(d)
    print(bn, "sold for",qty*100,"bucks")
    if bn.endswith("e"):
        print("\nstock increased by 5%!")
        stk=(stk*0.05)+stk
        d["stock"]=stk
        print(d)
    L.append(d)
    print("\n")
print(L)
bkn=input("book name: ")
for i in Lh:
    if i["book name"]==bkn:
        print(d["qty sold"], "pieces sold")
        break
    else:
        print("book not found")



