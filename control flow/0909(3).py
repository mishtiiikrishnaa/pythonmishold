#print some pattern, 9 sept(3)
num=int(input("give a number: "))
for factor in range(1, num):
     if num%factor==0:
        print(num, "isn't prime")
        break
     else:
        print(num,"is prime") 

