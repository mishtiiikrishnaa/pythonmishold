#to generate prime nos for a given range
ran1=int(input("range: "))
ran2=int(input("range2: "))
if ran1==1:
    ran1=2
for num in range(ran1,ran2):
    if num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
        print(num, end= " ")
    if num==2 or num==3 or num==5 or num==7:
        print(num, end= " ")
