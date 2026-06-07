lyst=eval(input("enter a number list: "))
rem=int(input("enter number to be removed: "))
if rem in lyst:
    lyst.remove(rem)                                                
print(lyst) #prints list with no "rem" value
ct=int(input("enter number: "))
print("frequency of", ct, "in given list is", lyst.count(ct)) #prints frequency of "ct" value in given list
lyst.reverse() #reverses the list without creating new variable
print(lyst) #prints reversed list
lyst.sort()
print(lyst) #prints ascending order of list
lyst.sort(reverse=True)
print(lyst) #prints descending order of list
lyst1=sorted(lyst) #"lyst1" becomes ascending order of "lyst"
print(lyst1)
lyst1=sorted(lyst,reverse=True) #"lyst1" becomes descending order of "lyst"
print(lyst1)
lyst1.clear(), lyst.clear() #"lyst" & "lyst1" become empty
print(lyst1,lyst)
