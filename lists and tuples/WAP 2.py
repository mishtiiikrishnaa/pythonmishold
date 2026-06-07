#WAP to read two lists of the same size, generate a new list which contains
#the sum of elements of first list and second list.
lyst1=eval(input("list 1: "))
lyst2=eval(input("list 2: "))
lyst3=[]
if len(lyst1)!=len(lyst2):
    print("error")
for number in range(len(lyst1)):
    lyst3.append(lyst1[number]+lyst2[number])
print(lyst3)
