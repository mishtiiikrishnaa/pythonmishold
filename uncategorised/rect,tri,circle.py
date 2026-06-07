inp=input("circle, triangle, or rectangle? ")
if inp in"circle":
    r=int(input("radius: "))
    print("area: ", 3.14*r*r)
elif inp in"triangle":
    b=int(input("base: "))
    h=int(input("height: "))
    print("area: ", (1/2)*b*h)
elif inp in "rectangle":
    l=int(input("length: "))
    b=int(input("breadth: "))
    print("area: ", b*l)
else:
    print("no")