#function w/ argument but w/out return
def f3(listarg):
    print("\t inside call function now")
    print("\t received: ",listarg)
    listarg[0]+=2
    print("\t\t listarg[0]+=2")
    print("\t given list within called function, after changes:",listarg)
list1=[1]
print("list before function call: ", list1)
f3(list1)
print("list after function call: ", list1)   
