#page 369, q(13)
lyst=eval(input("give a list: "))
range1=int(input("from: "))
range2=int(input("to: "))
maximum, minimum=0,0
for num in range(range1,range2+1):
    if lyst[num]>lyst[num-1]:
        maximum=lyst[num]
        minimum=lyst[num-1]
    elif lyst[num-1]>lyst[num]:
        minimum=lyst[num]
        maximum=lyst[num-1]
print("maximum value: ", maximum)
print("minimum value: ", minimum)
    
