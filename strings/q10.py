text="Welcome Python"
L=len(text)
ntext=" "
for i in range(0,L):
    if text[i].isupper():
        ntext=ntext+text[i].lower()
    elif text[i].isalpha():
        ntext=ntext+text[i].upper()
    else:
        ntext=ntext+"!"
print(ntext)