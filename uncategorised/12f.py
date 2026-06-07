a=50
b=20
for i in range(0,2):
    temp=a+b
    a+=temp
    if b!=200:
        print(temp, a , b)