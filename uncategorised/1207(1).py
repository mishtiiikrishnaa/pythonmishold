for m in range (0,3):
    print("enter 2 no.s: ")
    x=int(input("enter no. 1: "))
    y=int(input("enter no. 2: "))
    if y==0:
          print("the denominator can't be 0, give another number!")
    else:
        z=x//y
        print("quotient=",z)
