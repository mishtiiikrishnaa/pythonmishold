unit1=int(input("enter the initial power consumed: "))
unit2=int(input("enter the final power consumed: "))
unit=unit2-unit1
if unit<100:
    ct=unit*0.50
elif unit==101 and unit>101 and unit<200:
    ct=unit*1.00
elif unit==201 and unit>201 and unit<300:
    ct=unit*2.00
else:
    ct=unit*3.00
print("electricity charge",ct)
