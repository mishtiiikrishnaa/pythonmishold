#page 394, 16
tup=eval(input("enter a tuple: "))
for el in tup:
    if tup.count(el)>1:
        print("duplicate elements")
        break
