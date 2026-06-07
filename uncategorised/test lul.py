def Total (Num=10):
    Sum=0
    for C in range(1,Num+1):
        if C%2!=0:
            continue
     Sum+=C
    return Sum
print(Total(4),end="$")
print(Total(),sep="@")
