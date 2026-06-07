n = int(input("number: "))
f, s = 1, -1
th = f + s
print(th)
for i in range(n):
    f, s = th, f
    th, s = f, s
    th = f + s
    print(th)
