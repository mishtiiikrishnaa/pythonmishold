rge = int(input("enter the no. of variables you'd like: "))
x = int(input("enter 'x' value: "))
y = int(input("enter 'y' value: "))
total = 0
for power in range(0, rge + 1):
    fraction = x ** power / y ** power
    total = total+1
print(total)

