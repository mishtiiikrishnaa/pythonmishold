def ins(TN, bid, bkn, pri, qty):
    m="insert into {}(bookid, bookname, price, qty) values ('{}','{}',{},{})".format(TN, bid,bkn,pri,qty)
    cursor.execute(m)
    var.commit()

ch=int(input("menu: \n\t1. create table \n\t2. add records to 'library' \n\t3. display all records in table \n\t4. display records whose price is >500 \n\t5. display records whose quantity is <100 \n\t\t 1/2/3/4/5? "))

import mysql.connector as mc
var=mc.connect(host="localhost",user="root",passwd="123456",database="meghnanair")
if var.is_connected():
    print("connected")
else:
    print("not connected")
cursor=var.cursor()

if ch==1:
    tn=input("table name? ")
    St="create table {} (bookid varchar(20), bookname varchar (20), price integer, qty integer)".format(tn,)
    cursor.execute(St)

elif ch==2:
    t=input("table name? ")
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
    ins(t,bid,bkn,pri,qty)

elif ch==3:
    T=input("table name? ")
    print("display all records: ")
    st="select *from {}".format(T,)
    cursor.execute(st)
    d=cursor.fetchall()
    for i in d:
        print (i)

elif ch==4:
    p=input("table name? ")
    print("all books above the price of 500: ")
    s="select *from {} where price > {}".format(p,500)
    cursor.execute(s)
    da=cursor.fetchall()
    for j in da:
        print (j)

elif ch==5:
    l=input("table name? ")
    print("all books below the qty of 100: ")
    s1="select *from {} where qty < {}".format(l,100)
    cursor.execute(s1)
    D=cursor.fetchall()
    for k in D:
        print (k)

else:
    print("valid number?")




    
        

    
