#program 1, page 321
string=input("input a number with dashes in appropriate places: ")
nstring=str(string)
for ch in range(0,11):
    if ch[3]=="-" and ch[7]=="-":
        print("the given number is a valid number")
    else:
        print("the given number isn't a valid number")
        
