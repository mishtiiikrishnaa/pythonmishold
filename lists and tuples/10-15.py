#10.
s=eval(input("enter a tuple of strings: "))
for i in s:
    if len(i)>10:
        print(i)
#11.
t=eval(input("enter a tuple of numbers: "))
print(sum(t)/len(t))
#12.
u=eval(input("enter a tuple of numbers: "))
o,e=0,0
for j in u:
    if j%2==0:
        e+=1
    else:
        o+=1
print(e,o)
#13.
v=eval(input("enter a number tuple: "))
V=list(v)
V.sort()
print(V[-2])
#14.
p=eval(input("enter a number tuple: "))
n=int(input("number to search? "))
if n in p:
    print(p.index(n))
else:
    print(n, "not found")
#15.
t=[]
while True:
    T=eval(input("enter a tuple: "))
    t.append(T)
    c=input("enter more? y/n")
    if c=="y":
        c=True
print(tuple(t))

    


        
    

    
 
