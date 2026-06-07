text=list("SaVE EArth")
for i in range(0, len(text),2):
    if (text[i]=="A" or text[i]=="E"):
        text[i]="#"
    elif(text[i].islower()):
        text[i]=text[i].upper()
    else:
        text[i]="@"
print(text)