#program 5.5
fileinp=open("marks.txt")
while str:
    str=fileinp.readline()
    print(str)

#program 5.6
myfile=open("sample.txt")
line= " "
while line:
    line=myfile.readline()
    for word in line.split():
        print(word,end="#")
    print()


#program 5.7
ch= " "
vc,cc=0,0
while ch:
    ch=myfile.read(1)
    if ch.isalpha():
        if ch in ["aAeEiIoOuU"]:
            vc=+1
        else:
            cc+=1
print(vc,cc)
myfile.close()
    
