#page 385, 11.12
tup=eval(input("tuple: "))
ln=len(tup)
num=tup.count(tup[0])
if num==ln:
    print("all elements in tuple are same")
else:
    print("tuple has diff. elements")
