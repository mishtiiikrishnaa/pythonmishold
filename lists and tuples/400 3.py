#page 400[3]
n=int(input("how many numbers?"))
num=[]
for i in range(n):
          number=int(input("enter a number: "))
          num.append(number)
numt=tuple(num)
print(numt)
print("max:", max(numt),"\nmin:", min(numt))
