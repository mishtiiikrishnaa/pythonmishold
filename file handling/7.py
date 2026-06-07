#program 5.3
count=int(input("how many? "))
fileout=open("marks.txt","w")
for i in range(count):
    rollno=int(input("roll: "))
    name=input("name: ")
    marks=float(input("marks: "))
    rec=str(rollno)+","+name+","+str(marks)
    fileout.write(rec)
fileout.close()

#program 5.4
count=int(input("how many? "))
fileout=open("marks.txt","a")
for i in range(count):
    rollno=int(input("roll: "))
    name=input("name: ")
    marks=float(input("marks: "))
    rec=str(rollno)+","+name+","+str(marks)
    fileout.write(rec)
fileout.close()
