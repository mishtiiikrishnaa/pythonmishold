XIC, XIC75 = [], []
d1={}
nXIC = int(input("how many students in xi c? "))
for s in range(nXIC):
    S = {}
    print("student", s + 1, ":")
    S["name"] = input("name: ")
    S["roll_number"] = int(input("roll number: "))
    S["marks"] = int(input("marks: "))
    if S["marks"] > 75:
        XIC75.append(S)
    else:
        XIC.append(S)
print("students who scored above 75:")
for i in XIC75:
    print(i)
d1["students below 75"]=XIC
d1["students above 75"]=XIC75
print(d1)


