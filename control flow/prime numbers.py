SRANGE=int(input("enter a start value: "))
ERANGE=int(input("enter an end value: "))
print("prime numbers between", SRANGE, "and", ERANGE, "are:")
if SRANGE==1 or SRANGE==0:
    SRANGE=2
for number in range(SRANGE,ERANGE+1):
    if number==2 or number==5 or number==7 \
    or number==3:
        print(number, end=" ")
    if number % 2 != 0 and number % 3 != 0 \
            and number % 5 != 0 and number % 7 != 0:
        print(number, end=" ")