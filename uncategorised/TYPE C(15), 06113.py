#page 369, q(15)
lyst1=eval(input("a list: "))
lyst2=eval(input("another list: "))
if len(lyst1)!=len(lyst2):
    print("error!, input 2 lists of same size.")
for element in range(len(lyst1)):
    if lyst1[element]!=lyst2[element]:
        print("index where they differ:",element)
        break
