#2. WAP to read a list of strings & print only the strings that start with a vowel.
lyst=eval(input("enter a list of strings: "))
vowel=[]
for word in lyst:
    if word[0] in "aeiouAEIOU":
        vowel.append(word)
print("words that start with a vowel: ",vowel)
        
        
