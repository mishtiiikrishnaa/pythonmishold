#WAP to read a list and insert a given number in given index position. (condition: list length to be even)
lyst=eval(input("enter number list: "))
if len(lyst)%2==0:
    enter=int(input("enter number to insert: "))
    index=int(input("enter index number: "))
    lyst.insert(index,enter)
    print(lyst)
else:
    print("ok")
