#Input a list of numbers and swap elements at the even location with the elements at the odd location.
lyst=eval(input("enter a number list: "))
newlyst=[]
for num in range(1,len(lyst),2):
    newlyst.append(lyst[num])
    newlyst.append(lyst[num-1])
print("swapped list:", newlyst)