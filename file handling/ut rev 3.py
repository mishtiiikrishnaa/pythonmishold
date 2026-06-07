#code snippet 6
myfile=open("sample.txt")
str1=" "
size,tsize=0,0
while str1:
    str1=myfile.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())
print("size of file after removing eol char.s: ",tsize)
print("total size:", tsize)

#code snippet 7
s=myfile.readlines()
print(s)
