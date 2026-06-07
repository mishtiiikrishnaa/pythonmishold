L=input("enter some text: ")
print(list(L))
Lr=L.split()
print(Lr)
Lv,LC=[],[]
lv,lc=0,0
for it in Lr:
    if it[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        LC.append(it)
        lc+=1
    if it[-1] in "AEIOUaeiou":
        Lv.append(it)
        lv+=1
print("vowel ending words: ",Lv, "\ncount of words: ",lv)
print("capital starting words: ",LC, "\ncount of words: ",lc)
