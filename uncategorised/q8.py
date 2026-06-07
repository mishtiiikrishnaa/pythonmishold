def one(a,b):
     mo=min(str(a)[-1],str(b)[-1])
     if mo in str(a):
         return a
     elif mo in str(b):
         return b
n1,n2=int(input("n1: ")), int(input("n2: "))
print(one(n1,n2))
