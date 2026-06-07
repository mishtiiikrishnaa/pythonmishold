#Wap to read 2 tuples and join them.
#also extract the odd index pos value of 1st tuple
#and double their integer. also extract even pos value of 2nd tuple and
#half their integers. (consider only int values) and print updated tuple.
tp1=eval(input("enter tuple 1: "))
tp2=eval(input("enter tuple 2: "))
print(tp1+tp2)
ls1,ls2=list(tp1),list(tp2)
for i in range(1,len(ls1),2):
    ls1[i]*=2
for j in range(0,len(ls2),2):
    ls2[j]*=(1/2)
t1,t2=tuple(ls1),tuple(ls2)
print(t1+t2)
