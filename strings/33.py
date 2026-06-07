string=input("str: ")
for ch in range(0,len(string)):
    if ch%2==0:
        print(string[ch].upper(),end="")
    else:
        print(string[ch], end="")
