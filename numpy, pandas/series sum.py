x=int(input("x: "))
n=int(input("n: "))
sumt=0
xx=0
for y in range(1,n+1):
      xx=(x**y)/y
      sumt=sumt+xx
print(sumt)