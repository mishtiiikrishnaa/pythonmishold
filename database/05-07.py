import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="123456",database="meghnanair")
if mycon.is_connected():
    print("connected")

cursor=mycon.cursor()
cursor.execute("select * from books")
data=cursor.fetchall()
for row in data:
    print(row)
