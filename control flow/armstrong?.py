num=str(int(input("any number: ")))
total=0
for digit in num:
    total+=int(digit)**3
if total==int(num):
    print(num+" is an armstrong number")
else:
    print(num+" isn't an armstrong number")
