string=input("some string: ")
for character in string:
    if character.isdigit():
        print("there's digit(s) in here")
        break
else:
    print("there's no digits in here")
