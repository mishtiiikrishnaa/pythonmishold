#function w/out argument and no return
def fact():
         n=int(input("a number: "))
         j=1
         for i in range(1,n+1):
                  j*=i
         print(j)
fact()
