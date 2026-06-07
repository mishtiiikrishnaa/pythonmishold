#enter a list and do:
#[1,2,3,4],[2,1,4,3]
l=eval(input("enter a list: "))
if len(l)%2!=0:
         l=eval(input("enter a list of even length: "))
for i in range(len(l)):
         if i%2==0:
                  l[i],l[i+1]=l[i+1],l[i]
print(l)
