a,b,c=int(input("side a: ")), int(input("side b: ")), int(input("side c: "))
s=(a+b+c)/2
print("area=", ((s)*(s-a)*(s-b)*(s-c))**(1/2))

import math
a,b,c=int(input("side a: ")), int(input("side b: ")), int(input("side c: "))
s=(a+b+c)/2
print("area=", math.sqrt((s)*(s-a)*(s-b)*(s-c)))
