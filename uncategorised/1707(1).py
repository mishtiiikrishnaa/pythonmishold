first=-1
second=1
third=first+second
print(third)
for n in range (0,8):
    n=first
    first,second=second,third
    third,second=first,second
    third=second+third
    print(third)
print()
