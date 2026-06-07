n1 = int(input("a number: "))
n2 = int(input("another number: "))
n3 = int(input("another number: "))
if n1 > n2 > n3:
    print("2nd greatest: ", n2)
elif n1 > n3 > n2:
    print("2nd greatest: ", n3)
elif n2 > n1 > n3:
    print("2nd greatest: ", n1)
elif n3 > n2 > n1:
    print("2nd greatest: ", n2)
elif n2 > n3 > n1:
    print("2nd greatest: ", n3)
elif n3 > n1 > n2:
    print("2nd greatest: ", n1)
