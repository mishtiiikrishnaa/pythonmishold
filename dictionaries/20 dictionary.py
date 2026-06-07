XIC,XIC75=[],[]
nXIC=int(input("how many students in class xi c? "))
for s in range(nXIC):
    S={}
    print("student",s+1,":")
    S["name"]=input("name: ")
    S["roll_number"]=int(input("roll number: "))
    S["marks"]=int(input("marks: "))
    if S["marks"]>75:
        XIC75.append(S)
    else:
        XIC.append(S)
print("students who scored above 75:")
for i in XIC75:
    print(i)
    
