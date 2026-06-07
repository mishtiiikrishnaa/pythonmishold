#pg 352, 10.11
lyst=eval(input("list of numbers: "))
sub=eval(input("search for? "))
if sub in lyst:
    print(sub, "found at index", lyst.index(sub))
else:
    print(sub, "not found in", lyst)
