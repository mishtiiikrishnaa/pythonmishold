def conv(a): #void function
    print("$",a,"is",a*83.43,"rupees")
def conv1(a): #non void function
    return a*83.43
D=float(input("enter amount in dollars: "))
conv(D)
print("$",D,"is",conv1(D),"rupees")
    
    
    
