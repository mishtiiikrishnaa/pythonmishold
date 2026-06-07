#practicals q.18(not tuple)
#Input a list of numbers and swap elements at the even location with the elements at the odd location.
lyst=eval(input("enter a number list: "))
odd,even=0,0
for num in range(0,len(lyst)):
    if num%2==0:
        even=num
    else:
        odd=num
    lyst[odd],lyst[even]=lyst[even],lyst[odd]
print(lyst)
