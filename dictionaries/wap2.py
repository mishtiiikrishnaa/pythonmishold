#WAP using dictionary to enter 5 product details with product id as key, product name, qty, price as its values.
for i in range(5):
    d,d1={},{}
    pi=input("product id? ")
    d["product name"]=input("product name? ")
    d["qty"]=input("product quantity? ")
    d["price"]=input("product price? ")
    d1[pi]=d
    print(d1)

