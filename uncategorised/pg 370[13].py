#page 370, q(13)
lyst=eval(input("give a list: "))
range1=int(input("from: "))
range2=int(input("to: "))
lis=lyst[range1:range2]
lis.sort()
print("maximum value: ", lis[-1])
print("minimum value: ", lis[0])
    
