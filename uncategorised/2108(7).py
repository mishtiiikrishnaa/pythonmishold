numbers=" "
countodd=0
counteve=0
countneg=0
countpos=0
while True:
    numbers=int(input("enter a number: "))
    if numbers%2==0:
        counteve+=1
    elif numbers<0:
        countneg+=1
    elif numbers%2!=0:
        countodd+=1
    elif numbers>0:
        countpos+=1
    yes=input("would u like to continue, yes/no?: ")
    if yes=="yes":
        numbers=int(input("enter another number: "))
        if numbers%2==0:
            counteve+=1
        elif numbers<0:
            countneg+=1
        elif numbers%2!=0:
            countodd+=1
        elif numbers>0:
            countpos+=1
    else:
        print("count of odd numbers given:", countodd)
        print("count of even numbers given:", counteve)
        print("count of positive numbers given:", countpos)
        print("count of negative numbers given:", countneg)
