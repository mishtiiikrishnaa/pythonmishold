# WAP to use clear() and del() methods and write the difference between the two.
lyst=eval(input("give a list: "))
lyst1=lyst[:]
lyst2=lyst[:]
del lyst[0]
del lyst[-1]
print(lyst)
#del list_name[] here deletes values only at specified index positions.
del lyst1
#del list_name[] deletes the variable here, "lyst1" no longer exists after this point
lyst2.clear()
print(lyst2)
#clear() here deletes everything in lyst2, and takes no arguments
