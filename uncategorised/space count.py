string=input("some string: ")
count=0
for ch in string:
    if ch.isspace():
        count+=1
print(count)
