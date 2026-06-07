import csv
f=open('test.csv','w')
s=csv.writer(f)
s.writerow(['roll no','name','marks'])
for i in range(5):
    print('st rec:', (i+1))
    rollno=int(input("r.no:"))
    name=input("name:")
    marks=float(input("marks:"))
    sr=[rollno,name,marks]
    s.writerow(sr)
f.close()
l=open('test.csv')
x=csv.reader(l)
for i in x:
    print(i)
