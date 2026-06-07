input("student name: ")
print(f"max. marks: 100")
sub1=int(input("english marks: "))
sub2=int(input("math marks: "))
sub3=int(input("science marks: "))
sub4=int(input("hindi marks: "))
sub5=int(input("computer sci marks: "))
avg=sum([sub1,sub2,sub3,sub4,sub5])/5
print(f"the average scored is {avg} marks.")
if 90<=avg<=100:
    print(f"grade obtained: A")
elif 80<=avg<90:
    print(f"grade obtained: B")
elif 70<=avg<80:
    print(f"grade obtained: C")
elif 60<=avg<70:
    print(f"grade obtained: D")
else:
    print(f"grade obtained: E")
