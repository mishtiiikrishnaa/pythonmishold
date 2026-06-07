x="India 2023 - G20 summit"
print(x.split())
y=x.split('i')
z=y.partition('G')
t=y[0]+"@"+z[2]
print(t)
print(x.partition('20'))
print("@".join(x))
