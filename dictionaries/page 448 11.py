d1=eval(input("a dictionary: "))
d=eval(input("a dictionary: "))
D,D1=list(d1.items()), list(d.items())
b=[]
for i in D:
   if i in D1:
       b.append("yes")
if len(b)==len(d):
    print("d in d1")