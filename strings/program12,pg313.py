# page 313, program 12
string = input("give a word: ")
stringmod = " "
for character in range(0, len(string),2):
    stringmod += string[character]
    if character < len(string) - 1:
        stringmod += string[character + 1].upper()
print("string:", stringmod)
