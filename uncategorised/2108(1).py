#program 14, page 155, question bank
age=" "
countgr1, countgr2, countgr3=0,0,0 
while True:
    yes=input("would u like to start/continue, y/n?: ")
    if yes=="y":
            age=int(input("enter an age: "))
            if age<=35 and age>26:
                    countgr1+=1
            elif age>=36 and age<45:
                    countgr2+=1
            elif age>=46 and age<55:
                    countgr2+=1
    else:
        break 
print("employees aged between 26 and 35=", countgr1)
print("employees aged between 36 and 45=", countgr1)
print("employees aged between 46 and 55=", countgr1)
