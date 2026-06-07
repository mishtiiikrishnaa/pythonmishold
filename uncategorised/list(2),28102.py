x=eval(input("list: "))
oc,ec=0,0
for i in x:
    if i%2==0:
        ec+=1
    else:
        oc+=1
print("odd count: ", oc)
print("even count: ", ec)
