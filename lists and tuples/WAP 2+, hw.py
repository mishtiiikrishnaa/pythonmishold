#WAP to read 3 lists. find the maximum of list 2,
#add that to every element of list 1 and subtract it from every element of list 3.
#print the new list(s).
lyst1=eval(input("enter list 1: "))
lyst2=eval(input("enter list 2: "))
lyst3=eval(input("enter list 2: "))
greatest=0
for alphabet in range(len(lyst2)):
        if lyst2[alphabet]>lyst2[alphabet-1]:
                greatest=lyst2[alphabet]
        elif lyst2[alphabet]<lyst2[alphabet-1]:
                greatest=lyst2[alphabet-1]
print(greatest)
print("new lists:")
for number in range(len(lyst1)):
        lyst1[number]=lyst1[number]+greatest
for num in range(len(lyst3)):
        lyst3[num]=lyst3[num]-greatest
print("list 1:",lyst1)
print("list 3:",lyst3)





