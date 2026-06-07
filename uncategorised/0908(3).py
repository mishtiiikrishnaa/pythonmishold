string=input("give whatever you like:" )
upper, lower=0, 0
for character in string:
    if character.isupper():
        upper=upper+1
    elif character.islower():
        lower+=1
print("no. of uppercases:", upper)
print("no. of lowercases:", lower)
               
