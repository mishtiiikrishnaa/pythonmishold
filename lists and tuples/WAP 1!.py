#WAP to read book name and author as long as the user wants. create a list with sublists
while True:
    b=input("enter book name: ")
    a=input("enter author name: ")
    lyst0,lyst1=[],[]
    lyst0=lyst0.append(b)
    lyst1=lyst0.append(a)
    lyst=lyst.append(lyst1)
    c=input("do you want to do more? y/n:")
    if c=="y":
        h=True
    else:
        print(lyst)
    
