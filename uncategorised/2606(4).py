#all operations
print("s=sum")
print("d=difference")
print("p=product")
print("q=division")
print("e=exponent product")
print("r=remainder")
print("m=integer division")
inp=input("what operation from above?")
if inp=="s":
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    print(a+b)
elif inp=="d":
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    print(a-b)
elif inp=="p":
    e=int(input("enter a number: "))
    f=int(input("enter another number: "))
    print(a*b)
elif inp=="q":
    g=int(input("enter a number: "))
    h=int(input("enter another number: "))
    print(a/b)
elif inp=="e":
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    print(a**b)
elif inp=="r":
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    print(a%b)
else:
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    print(a//b)


