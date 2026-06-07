def tup(tuple):
    e,o=0,0
    for i in tuple:
        if i%2==0:
            e+=1
        elif i%2!=0:
            o+=1
        else:
            pass
    print("number of odd numbers: ",o)
    print("number of even numbers: ",e)
t=eval(input("enter a tuple of numbers: "))
tup(t)
