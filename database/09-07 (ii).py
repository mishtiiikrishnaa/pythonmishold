def ins(bid, bkn, pri, qty):
    m="insert into library(bookid, bookname, price, qty) values ('{}','{}',{},{})".format(bid,bkn,pri,qty)
    cursor.execute(m)
    var.commit()

ch=int(input("menu: \n\t1. add records to 'library' \n\t2. display all records in 'library' \n\t3. display records whose price is >500 \n\t4. display records whose quantity is <100 \n\t\t 1/2/3/4? "))

import mysql.connector as mc
var=mc.connect(host="localhost",user="root",passwd="123456",database="meghnanair")
if var.is_connected():
    print("connected")
else:
    print("not connected")
cursor=var.cursor() 

if ch==1:
    print("adding records:")
    while True:
        bid=input("book id: ")
        bkn=input("book name: ")
        pri=float(input("price: "))
        qty=int(input("quantity: "))
        c=input("more? y/n: ")
        if c!="y":
            break
        else:
            True
    ins(bid,bkn,pri,qty)

elif ch==2:
    print("display all records: ")
    st="select *from library"
    cursor.execute(st)
    d=cursor.fetchall()
    for i in d:
        print (i)

elif ch==3:
    print("all books above the price of 500: ")
    s="select *from library where price > {}".format(500,)
    cursor.execute(s)
    da=cursor.fetchall()
    for j in da:
        print (j)

elif ch==4:
    print("all books below the qty of 100: ")
    s1="select *from library where qty < {}".format(100,)
    cursor.execute(s1)
    D=cursor.fetchall()
    for k in D:
        print (k)

else:
    print("valid number?")




    
        

    
