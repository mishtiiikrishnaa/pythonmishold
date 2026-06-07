#armstrong number?
num=int(input("enter a number: "))
strnum=str(num)
tot=0
sumt=0
for ch in strnum:
    dig=int(ch)**3
    sumt+=dig
if sumt==num:
    print(num, "is an armstrong number")
else:
    print(num, "isn't an armstrong number")
