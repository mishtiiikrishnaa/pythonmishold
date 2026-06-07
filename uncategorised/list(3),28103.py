x=eval(input("list: "))
fd,nfd=0,0
for i in x:
    if i%5==0:
        fd+=1
    else:
        nfd+=1
print("divisible by 5: ", fd)
print("not divisible by 5: ", nfd)
