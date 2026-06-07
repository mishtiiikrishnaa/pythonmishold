#enter a list and print its reverse(with & without slicing & second list)
l=eval(input("enter a list: "))
print(l[::-1])
n=len(l)
for i in range(n):
         for j in range(i-1):
                  l[j],l[j-n]=l[j-n],l[j]
print(l)
