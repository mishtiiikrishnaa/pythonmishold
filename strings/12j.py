ch= "Our 3 Boys"
string= " "
for p in range(0, len(ch)-1):
    if ch[p].isdigit():
        string+="-"
    elif ch[p]==" ":
        string+="*"
    elif ch[p].isupper():
        string+=ch[p].lower()
    elif ch[p].islower():
        string+=ch[p+1].upper()
print(list(string))