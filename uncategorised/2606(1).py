#getting choice from user
print("a=perimetre of a rectangle")
print("b=volume of a sphere")
print("c=volume of a cone")
vol=input("choose: perimetre of a rectangle, volume of sphere, or volume of a cone? ")
if vol=="a":
    l=int(input("enter a length: "))
    b=int(input("enter a breadth: "))
    print (2*(l+b)) 
elif vol=="b":
    r1=int(input("enter a radius: "))
    print (4/3*3.14*r1*r1)
else:
    r2=int(input("enter another radius: "))
    h=r2=int(input("enter height: "))
    print ((3.14*r2*r2*h)/3)
