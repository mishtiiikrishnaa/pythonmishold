string=input("enter string: ")
if string[0:1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(string.upper())
elif string[1:2] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(string.upper())
elif string[2:3] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(string.upper())
elif string[3:4] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(string.upper())
else:
    print(string)