n1=int(input("first number"))
n2=int(input("second number"))
if n1>n2:
    larger=n1
else:
    larger=n2
lcm=0
while True:
    if larger%n1==0 and larger%n2==0:
        lcm=larger
    break
print(lcm)
print((n1*n2)/lcm)

