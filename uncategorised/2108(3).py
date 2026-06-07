#program 43, page 156, question bank
end=int(input("enter an end value: "))
for number in range(1, end+1):
    if number%2!=0:
        print(number, end=", ")
    else:
        print(-1*number, end=", ")
    if number==end:
        print("done; thank you")
