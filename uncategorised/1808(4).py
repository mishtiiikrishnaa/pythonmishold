#program 5, page 321
string=input("input a string: ")
digit=0
for ch in string:
    if ch.isdigit():
        print (ch)
        digit+=1
    else:
        print("there're no digits in here") 
print("og string: ", string)
print("sum of digits: ", digit)

        
