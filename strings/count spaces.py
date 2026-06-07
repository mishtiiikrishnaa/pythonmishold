line=input("a line: ")
print("count of spaces: ", len(line.split())-1)
c=0
cl=line
for ch in cl:
   if ch.isspace():
       c+=1
print(c)