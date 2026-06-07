s1=float(input("eng marks: "))
s2=float(input("math marks: "))
s3=float(input("sci marks: "))
s4=float(input("soc marks: "))
s5=float(input("hin marks: "))
tot=s1+s2+s3+s4+s5
avg=tot/5
print("total:",tot,"and avg:",avg)
if (avg<100) and (avg>=90):
    print(avg,"A1")
elif (avg<89) and (avg>=80):
    print(avg,"A2")
elif (avg<79) and (avg>=70):
    print(avg,"B1")
elif (avg<69) and (avg>=70):
    print(avg,"B2")
elif (avg<59) and (avg>=60):
    print(avg,"C1")
else:
    print(avg,"E")

