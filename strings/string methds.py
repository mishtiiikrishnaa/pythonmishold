string=input("give a string: ")
upper,lower,digit,space=0,0,0,0
for character in string:
    if character.isupper():
        upper+=1
    elif character.islower():
        lower+=1
    elif character.isdigit():
        digit+=1
    elif character.isspace():
        space+=1
print("uppercase characters:", upper)
print("lowercase characters:", lower)
print("digits:", digit)
print("spaces:", space)
print(len(string))
print(string.capitalize())
print(string.title())
print(string.swapcase())
print(string[::-1])
print(string[1::2])
print(string[-1::-2])
print("commas: ", string.count(","))
print(string.find("e"))
print(string.isalnum())
print(string.isalpha())
print(string.lower())
print(string.upper())
print(string.lstrip())
print(string.rstrip())
print(string.strip())
print(string.startswith("!"))
print(string.endswith("!"))
print(string.istitle())
print(string.replace(" ", "#"))
print(string.split())
print(string.partition("e"))
print(".".join(string))
print(string.join("*"))
print(string.index("#"))