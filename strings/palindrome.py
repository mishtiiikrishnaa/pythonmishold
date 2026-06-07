word=input("give a string: ")
if word==word[-1::-1]:
    print(word, "is a palindrome")
else:
    print(word, "isn't a palindrome")