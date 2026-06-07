num1=int(input("give a number: "))
num2=int(input("give a 2nd number: "))
num3=int(input("give a 3rd number: "))
if num1>num2 and num1>num3:
    print(f"{num1} is the greatest of {num1}, {num2} & "
          f"{num3}")
elif num2>num3 and num2>num1:
    print(f"{num2} is the greatest of {num1}, {num2} & "
          f"{num3}")
elif num3>num1 and num3>num2:
    print(f"{num3} is the greatest of {num1}, {num2} & "
          f"{num3}")
elif num1==num2==num3:
    print(f"{num1}={num2}={num3}")
