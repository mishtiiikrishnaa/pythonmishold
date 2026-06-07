count=sum=0
ans='y'
while ans=='y':
    number=int(input("number: "))
    if number<0:
        print("number entered is <0, aborting task!")
        break
    sum=sum+number
    count=count+1
    ans=input("wish to enter more numbers? (y/n)..")
else:
    print("you entered", count, "number(s) so far.")
print("sum of numbers entered is", sum)
