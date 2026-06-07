#detecting stuff
var=input("give a string: ") 
upper,lower,digit,space,special=0,0,0,0,0
for character in var:
    if character.isupper():
        upper+=1
    elif character.islower():
        lower+=1
    elif character.isdigit():
        digit+=1
    elif character.isspace():
        space+=1
    else:
        special+=1
print("the no. of uppercase characters in", var, "is", upper)
print("the no. of lowercase characters in", var, "is", lower)
print("the no. of digits in", var, "is", digit)
print("the no. of spaces in", var, "is", space)
print("the no. of special characters in", var, "is", special)
