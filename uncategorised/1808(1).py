#program 1, page 321
string=input("input a string: ")
character=input("input a particular string: ")
c_count=0
for cno in string:
    if cno==character:
        c_count+=1
print("no. of times", "'", character, "'" " occurs in", "'" ,string, "'" " is", c_count)
        
