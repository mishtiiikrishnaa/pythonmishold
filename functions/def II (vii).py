#function w/ argument but w/out return
def f3(listarg):
    print("\t inside call function now")
    print("\t received: ",listarg)
    listarg.append(2)
    listarg.extend([5,1])
    print("\t\tlistarg.append(2)\n\t\tlistarg.extend([5,1])")
    print("\tgiven list after adding elements:",lsitarg)
    listarg.remove(5)
    print("\t\tlistarg.remove(5)")
    print("\t given list within called function, after changes:",listarg)
list1=[1]
print("list before function call: ", list1)
f3(list1)
print("list after function call: ", list1)
