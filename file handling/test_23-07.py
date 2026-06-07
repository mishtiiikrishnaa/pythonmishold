fh=open("test.txt")
print(fh.read(30))
print(fh.read(600))
print(fh.read(6))
for i in fh.readlines():
    print(i)


