#code snippet 1
myfile=open("sample.txt")
str=myfile.read(30)
print(str)

#code snippet 2
str2=myfile.read(50)
print(str2)

#code snippet 3
str3=myfile.read()
print(str3)

#code snippet 4
str4=myfile.readline()
print(str4,end=" ")
str4=myfile.readline()
print(str4,end=" ")
str4=myfile.readline()
print(str4,end=" ")

#code snippet 5
STR= " "
while STR:
    STR=myfile.readline()
    print(STR, end= " ")

#code snippet 5.alt
for line in myfile:
    print(line)





