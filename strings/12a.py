S="ObjeCT"
L=len(S)
S1=" "
print(S.swapcase())
for C in range(0,L):
    if S[C].islower():
        S1+=S[C].upper()
    elif (C%2==0):
        S1+="E"
    else:
        S1+=S[C].lower()
print(S1)