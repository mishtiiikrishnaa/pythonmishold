#function w/ argument but w/out return
def f4(listarg):
    print("\t inside call function now")
    print("\t received: ",listarg)
    new=[3,5]
    listarg=new
    listarg.append(6)
    print("\t\tnew=[3,5]\n\t\tlistarg=new\n\t\tlistarg.append(6)")
    print("\t given list within called function, after changes:",listarg)
list1=[1,4]
print("list before function call: ", list1)
f4(list1)
print("list after function call: ", list1)   
