import mysql.connector as mc
var=mc.connect(host="localhost",user="root",passwd="123456",database="meghnanair")
if var.is_connected():
    print("connected")
else:
    print("not connected")
cursor=var.cursor()
cursor.execute("select * from books where price > %s"%(500,))
data=cursor.fetchall()
for j in data:
    print (j)
d="select * from books where price > {}".format(500,)
cursor.execute(d)
Data=cursor.fetchall()
for i in Data:
    print(i)

