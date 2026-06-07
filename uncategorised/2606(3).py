#quiz score
s=0
print("answer in true/false, wherein:")
print("t=true")
print("f=false")
q1=input("area of a rectangle=l*b ")
if q1=="t":
    tot=s+1
else:
    tot=s
q2=input("area of a square=l**3 ")
if q2=="f":
    tot2=tot+1
else:
    tot2=tot
q3=input("the British never came to India. ")
if q3=="f":
    tot3=tot2+1
else:
    tot3=tot2
q4=input("there's no racial discrimination today. ")
if q4=="f":
    tot4=tot3+1
else:
    tot4=tot3
q5=input("there are 7 continents today ")
if q5=="t":
    tot5=tot4+1
else:
    tot5=tot4
print("total score: ",tot5)
