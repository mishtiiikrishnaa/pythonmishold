#program 9.10 page 305
line=input("give a line: ")
lower,upper,alphas,digits,symbols=0,0,0,0,0
for character in line:
    if character.islower():
        lower+=1
    elif character.isupper():
        upper+=1
    elif character.isdigit():
        digits+=1
    elif character.isalpha():
        alphas+=1
    elif character.isalnum()!=True and character!=" ": 
        symbols+=1
print("uppercase character count: ", upper) 
print("lowercase character count: ", lower)
print("digit count: ", digits)
print("alphabet count: ", alphas) 
print("symbol count: ", symbols)
      
