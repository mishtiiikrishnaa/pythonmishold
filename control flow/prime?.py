num=int(input("number: "))
if num==2 or num==3 or num==5 or num==7:
    print("prime")
else:
    for fact in range(2, num):
        if num % fact == 0:
            print("not prime")
            break
        else:
            print("prime")
            break
