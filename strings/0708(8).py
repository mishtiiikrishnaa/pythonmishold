#palindrome
string=input("enter what's on your mind: ")
string1=0
for ch in range(len(string)):
    if ch==string:
        string1=string+1
print(string + " is a palidrome, nice!")
    #else:
        #print(string + "aint a palindrome :(")
