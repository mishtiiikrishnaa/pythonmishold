#page 370, q(6)
lyst=eval(input("enter a list of numbers: "))
number=int(input("number to check: "))
if number in lyst:
    print("postion of", number, ":",lyst.index(number))
else:
    print(number, "not found")
