#menu driven program for binary to decimal & decimal to octal
while True:
    print("MENU: ")
    print("1. binary to decimal")
    print("2. binary to octal")
    print("")
    choosen=input("1 or 2? ")
    print("")
    if choosen=="1":
        print("binary to decimal conversion.")
        binnum=int(input("enter a binary number: "))
        if str(binnum) in "01":
            deci=0
            while binnum>0:
                for power in range(len(str(binnum))):
                    deci=deci+(binnum%10)*(2**power)
                    binnum=binnum//10
            print(str(deci)[::-1])
        else:
            print("error! enter a binary number.")
    elif choosen=="2":
        print("decimal to octal conversion.")
        decnum=int(input("enter a decimal number: "))
        octa=" "
        while decnum>0:
                octa=octa+str((decnum%8))
                decnum=decnum//8
        print(str(octa)[::-1])
    print("")
        
