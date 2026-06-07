d=eval(input("enter a dictionary: "))
m={}
for key, value in d.items():
    m[value]=key
print(m)