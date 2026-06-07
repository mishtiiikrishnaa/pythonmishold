word=input("give a string containing lowercase, uppercase and digits: ")
upper, lower, digit=0, 0, 0
for ch in word:
    if ch.isupper():
        upper=upper+1
    if ch.islower():
        lower=lower+1
    if ch.isdigit():
        digit=digit+1
print("the no. of uppercase characters in", word, "is", upper)
print("the no. of lowercase characters in", word, "is", lower)
print("the no. of digits in", word, "is", digit)

