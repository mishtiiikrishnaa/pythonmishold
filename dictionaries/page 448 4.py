l={}
while True:
    G=[]
    tn=input("enter team name: ")
    gw=int(input("games won: "))
    gl=int(input("games lost: "))
    G.extend([gw,gl])
    l[tn]=G
    c=input("enter more teams? y/n ")
    if c=="y":
        c=True
    else:
        break
TN=input("enter team name: ")
if TN in l:
    print(100*(l[tn][0]/sum(l[tn])))
L=[]
for i in l:
    L.append(l[i])
