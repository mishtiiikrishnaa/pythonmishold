#print some sum, 9 sept(5)
rage=int(input("give some range: "))
for number in range(1, rage):
    for multiplier in range(2, number,2):
        print(number*multiplier)
