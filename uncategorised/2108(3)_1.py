#program 14, page 155, question bank
numbers=" "
countodd=0
counteve=0
countneg=0
countpos=0
while True:
    numbers=int(input("enter a number: "))
    if numbers%2:
        counteve+=1
    else:
        countodd+=1
    if numbers==numbers*-1:
        countneg+=1
    else:
        countpos+=1
    yes=input("would u like to continue, y/n?: ")
    if yes=="y":
        numbers=int(input("enter a number: "))
        if numbers%2:
            counteve+=1
        else:
            countodd+=1
        if numbers==numbers*-1:
            countneg+=1
        else:
            countpos+=1
    else:
        print("count of odd numbers given:", countodd)
        print("count of even numbers given:", counteve)
        print("count of positive numbers given:", countpos)
        print("count of negative numbers given:", countneg)
    break 
        
