Text="Mind@Work!"
s=" "
for i in range(0, len(Text)):
    if (Text[i].isalpha()==False):
        s+="*"
    elif (Text[i].isupper()):
        s+=chr(ord(Text[i])+1)
    else:
        s+=Text[i+1]
print(s)
