num=str(int(input("some number: ")))
tot=0
for dig in num:
    tot=tot+int(dig)
print("the sum of all the digits in "+ num +
      " is "+ str(tot))