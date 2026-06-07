n1=int(input("input no1: "))
n2=int(input("input no2: "))
n3=int(input("input no3: "))
if (n1==n2 and n1!=3) or (n1==n3 and n1!=2) or (n2==n3 and n2!=n1):
    if n1>n3:
        print(n1)
    elif n3>n1:
        print(n3)
    elif n1>n2:
        print(n1)
    elif n2>n1:
        print(n2)
else:
    if n1>n2 and n1>n3:
        print(n1)
    elif n2>n3 and n2>n1:
        print(n2)
    elif n3>n2 and n3>n1:
        print(n3)
