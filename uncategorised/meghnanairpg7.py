def fun(list):
    for i in range(len(list)):
        if i%2==0:
            list[i]*=(1/2)
        else:
            list[i]*=2
    print('new list: ',list)
l=eval(input("enter a list: "))
fun(l)
