for num in range(15,25):
    for i in range(2,num):
        if num%i==0:      #determining factors
            j=num/1
            print("found a factor(",i,") for", num)
            break         #needn't continue, factor found
    else:                 #else part of inner loop
        print(num,"is a prime number")
