myfile=open("sample.txt")
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
