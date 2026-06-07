number = int(input("enter a number w/ 3 digits: "))
totev = 0
totod = 0
no1 = number // 100
if no1 % 2 == 0:
    totev = totev + no1
else:
    totod = totod + no1
no2_1 = number % 100
no2 = no2_1 // 10
if no2 % 2 == 0:
    totev = totev + no2
else:
    totod = totod + no2
no3 = number % 10
if no3 % 2 == 0:
    totev = totev + no3
else:
    totod = totod + no3
print("the sum of even digits is", totev, ", while the sum of odd digits is", totod)
