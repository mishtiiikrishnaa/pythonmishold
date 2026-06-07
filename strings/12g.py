message="Python Programming"
s= " "
length=len(message)
for i in range(0, length):
    if i%2==0:
        s+=message[i].upper()
    else:
        s+=message[i]
print(s, "#", i)